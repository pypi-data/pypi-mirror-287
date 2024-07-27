import os
import math
import json
import datetime
import logging

from ..helpers import responsify
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc, or_, and_, cast, func
from sqlalchemy.sql import expression
from sqlalchemy.dialects import postgresql
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.types import (
    Date,
    String,
    Integer,
    Boolean,
    DateTime,
    Time,
    Numeric,
)
from sqlalchemy.orm import aliased
from sqlalchemy.ext.declarative import declared_attr

from zephony.exceptions import InvalidRequestData

from zephony.helpers import(
    is_valid_date,
    is_valid_datetime,
    get_rows_from_csv,
    serialize_datetime,
    time_format,
    date_format,
    datetime_format,
    datetime_with_microseconds_format,
    datetime_with_microseconds_and_timezone_format,
)

db = SQLAlchemy()
logger = logging.getLogger(__name__)

class BaseModel(db.Model):
    __abstract__ = True

    id_ = db.Column('id', db.BigInteger, primary_key=True)
    token = db.Column(db.String, unique=True, index=True)
    is_deleted = db.Column(db.Boolean, server_default=expression.false())
    deleted_data = db.Column(JSONB)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    last_updated_at = db.Column(db.DateTime(timezone=True))
    deleted_at = db.Column(db.DateTime(timezone=True))
    # id_creator_user = db.Column(db.BigInteger, index=True)
    # id_last_updated_user = db.Column(db.BigInteger, index=True)
    # id_deleted_user = db.Column(db.BigInteger)
    # id_organization = db.Column(db.BigInteger)

    @declared_attr
    def id_creator_user(cls):
        return db.Column(
            db.BigInteger,
            db.ForeignKey('users.id')
        )

    @declared_attr
    def id_last_updated_user(cls):
        return db.Column(
            db.BigInteger,
            db.ForeignKey('users.id')
        )

    @declared_attr
    def id_deleted_user(cls):
        return db.Column(
            db.BigInteger,
            db.ForeignKey('users.id')
        )

    @declared_attr
    def id_organization(cls):
        return db.Column(
            db.BigInteger,
            db.ForeignKey('organizations.id')
        )

    readable_fields = []
    updatable_fields = []
    filterable_fields = []

    # TODO: Do assignments by doing datatype conversions for datetime, etc
    def __init__(self, data, from_seed_file=False, update_time=True):
        for key, value in data.items():
            # ic(key)
            if hasattr(self, key):
                # ic('Yes')
                if from_seed_file:
                    setattr(self, key, None if value == '' else value)
                else:
                    setattr(self, key, value)
            else:
                # ic('No')
                logger.info(f'{type(self).__name__} Model has no attribute : {key}')

        created_at = datetime.datetime.now(datetime.timezone.utc)
        self.created_at = created_at
        if update_time:
            self.last_updated_at = created_at

        if request and request.user and request.user.id_:
            self.id_creator_user = request.user.id_

        if request and request.user and request.user.id_organization:
            self.id_organization = request.user.id_organization

        db.session.add(self)
        db.session.flush()

    # TODO: Needs refactoring
    @staticmethod
    def _add_key_from_csv_row(data, k, v, row):
        if type(v) == tuple:
            if len(v) == 1:  # Value hardcoded right in the index being sent
                data[k] = v[0]
            elif len(v) == 2:  # Value has to be type casted
                # Do nothing if value is empty
                if not row[v[0]].strip():
                    return

                if v[1] is int:
                    data[k] = int(row[v[0]].split('.')[0])
                elif v[1] is bool:
                    if row[v[0]] in ['true', 1, '1', '1.0', 'TRUE', 'True']:
                        data[k] = True
                    elif row[v[0]] in ['false', 0, '0', '0.0', 'FALSE', 'False']:
                        data[k] = False
                    else:
                        data[k] = None
                elif v[1] == 'datetime':
                    try:
                        date_str_format = '%d/%m/%Y' if '/' in row[v[0]] else '%Y-%m-%d'
                        data[k] = datetime.datetime.strptime(row[v[0]], date_str_format).isoformat()
                    except ValueError:
                        #TODO: Doing this only to make import work quickly
                        data[k] = None
                        # raise ValueError('`{}`: Cannot parse datetime'.format(row[v[0]]))
                elif v[1] == 'datetime_iso':
                    try:
                        date_str_format = '%d/%m/%Y' if '/' in row[v[0]] else '%Y-%m-%d'
                        data[k] = datetime.datetime.strptime(row[v[0]], date_str_format).isoformat()
                    except ValueError:
                        #TODO: Doing this only to make import work quickly
                        data[k] = None
                        # raise ValueError('`{}`: Cannot parse datetime'.format(row[v[0]]))
                elif callable(v[1]):
                    data[k] = v[1](row[v[0]])
                else:
                    raise ValueError('`{}`: Unsupported type to type case to'.format(v[1]))
            elif len(v) == 3:
                if v[2] == 'power_of_2':  # Used for permissions to calculate & store permission bit
                    # Permission bit cannot be empty
                    if not row[v[0]].strip():
                        raise ValueError('Permission bit value cannot be empty')

                    if v[1] is not int:
                        raise ValueError('`{}`: Cannot type cast to integer'.format(v[1]))

                    data[k] = str(2 ** ((int(row[v[0]].split('.')[0])) - 1))
                elif v[2] == 'boolean':
                    if row[v[0]].strip() == 'x':
                        data[k] = True
                    else:
                        data[k] = False
                elif v[2] == 'permission_tokens':
                    # Queries permissions table
                    from .permission import Permission
                    permissions_map = Permission.get_map()

                    permission_bit_sequence = 0
                    # Split by comma
                    if row[v[0]].strip():
                        permission_tokens = row[v[0]].strip().split(',')
                        for token in permission_tokens:
                            permission_bit_sequence |= int(permissions_map[token.strip()])

                    data[k] = str(permission_bit_sequence)
                elif v[2] == 'foreign_key':  # For foreign key relationships
                    cls = v[1]

                    # Query and get the object ID, if found, else, create new entry in the database and return the ID.
                    obj = cls.query.filter_by(
                        original_name=row[v[0]],
                        is_deleted=False
                        # status='active'
                    ).first()

                    if not obj:
                        obj = cls({
                            'original_name': row[v[0]]
                        })
                        db.session.add(obj)
                        db.session.commit()

                    data[k] = obj.id_
                else:
                    raise Exception('Invalid value: `{}`'.format(v[2]))
            else:
                raise Exception('Invalid tuple length: `{}`'.format(len(v)))
        else:
            data[k] = row[v]

    def _get_base_details(self):
        base_details = {
            'id': self.id_,
            'token': self.token,
            # 'created_at': serialize_datetime(
            #     self.created_at,
            #     datetime_with_microseconds_and_timezone_format,
            # ),
            'created_at': str(self.created_at.isoformat())
        }
        if self.last_updated_at:
            # base_details['last_updated_at'] = serialize_datetime(
            #     self.last_updated_at,
            #     datetime_with_microseconds_and_timezone_format,
            # )
            base_details['last_updated_at'] = str(self.last_updated_at.isoformat())
        else:
            base_details['last_updated_at'] = None

        return base_details

    @staticmethod
    def _convert_filters_map_to_list(filter_map):
        """
        Each filter parameter has a filter operator (starts_with,
        ends_with, etc.) and a field name. If a operator is not
        present, `equals` is used as the default operator.

        The filter parameter takes the following format:
            __<filter_operator>__<field_name>

        For example, if you want to get users who are younger than 20,
        you can use the filter parameter `__lesser_than__age` where
        `lesser_than` is the operator and `age` is the field name.

        The following filter parameter formats are allowed:

            1. Type: VARCHAR
                - __starts_with__<field_name>
                - __ends_with__<field_name>
                - __contains__<field_name>
                - __equals__<field_name>
            2. Type: INTEGER
                - __lesser_than__<field_name>
                - __greater_than__<field_name>
                - __equals__<field_name>
            3. Type: BOOLEAN
                - __equals__<field_name>
            4. Type: DATETIME
                - __from__<field_name>
                - __to__<field_name>
                - __equals__<field_name>

        Returns [{
            'key': <field_name>,
            'values': [<value1>, <value2>],
            'operator': <filter_operator>,
        }]
        """

        filters_list = []
        for filter_key_with_operator in filter_map:
            if filter_map[filter_key_with_operator] == None:
                continue
            # If multiple values are present in the filter,
            # use a comma to separate them.
            filter_map[filter_key_with_operator] = filter_map[
                filter_key_with_operator
            ].strip('[] ')
            if ',' in filter_map[filter_key_with_operator]:
                values = filter_map[filter_key_with_operator].split(',')
            else:
                values = [ filter_map[filter_key_with_operator] ]

            filter_ = {
                'key': None,
                'values': [v.strip(' ') for v in values],
                'operator': None,
            }
            if filter_key_with_operator.startswith('__'):
                # First segment will be an empty string
                segments = filter_key_with_operator.split('__')[1:]
                filter_['operator'] = segments[0]
                filter_['key'] = segments[1]
            else:
                filter_['operator'] = 'equals'
                filter_['key'] = filter_key_with_operator

            filters_list.append(filter_)

        return filters_list

    # TODO: Needs refactoring
    @classmethod
    def load_from_csv(cls, f_path, column_index, delimiter=',', header=True,
            empty_check_col=1, repr_col=1, row_commit=False):
        """
        This function takes a relative path of a csv file and populates
        the database with the contents of the csv file.

        :param str f_path: The relative path to the file
        :param dict column_index: Model field_name, CSV index mapper
        :param bool header: Flag to determine whether to skip first line of CSV
        :param int empty_check_col: The column count if empty marks last line of CSV
        :param int repr_col: The value to be printed for each row in log messages
        :param bool row_commit: If True, commit immediately after adding to session

        :return bool: True
        """

        objects = []
        duplicates = []
        rows = get_rows_from_csv(
            f_path,
            delimiter=delimiter,
            header=header,
            empty_check_col=empty_check_col,
        )
        for row_index, row in enumerate(rows):
            # logger.debug('Loading {} `{}` from CSV..'.format(cls.__name__, row[repr_col]))
            data = {}
            for k, v in column_index.items():
                if type(v) == dict:  # Handling nested dictionary
                    data[k] = {}
                    for sk, sv in v.items():  # sk: sub_key, sv: sub_value :P
                        cls._add_key_from_csv_row(data[k], sk, sv, row)
                else:
                    cls._add_key_from_csv_row(data, k, v, row)

            # The following try-except block applies only for user
            # Skip row if error occurs
            try:
                obj = cls(data, from_seed_file=True)
            except InvalidRequestData as e:
                if hasattr(e, 'duplicate') and e.duplicate:
                    duplicates.append(e.duplicate.get_details())
                e.row = row_index
                continue
            # except:
            #     ic('k', db.session.execute('SHOW search_path').scalar())
            #     ...
            db.session.add(obj)

            if row_commit:
                try:
                    db.session.commit()
                except Exception as e:
                    print(e)
                    db.session.rollback()

            objects.append(obj)

        res = {
            'objects': objects,
            'total_non_empty_rows': len(rows),
        }

        if duplicates:
            res['duplicates'] = duplicates

        return res

    @classmethod
    def add_filters_to_query(cls, q, filters_map, filterable_fields):
        # Convert filters map to filters list
        filters = cls._convert_filters_map_to_list(filters_map)

        if os.environ.get('APP_ENV', None) != 'live':
            # logger.info('----------------------------------------')
            # logger.info(f'Filters to be applied : {filters}')
            pass

        for filter_ in filters:
            if filter_['key'] in filterable_fields:
                filter_attr = filterable_fields[f"{filter_['key']}"]
                field_type = filter_attr.type
                logger.info(f'Trying to apply filter : {filter_}')
            else:
                logger.info(f'Ignoring invalid filter key : {filter_["key"]}')
                continue

            if isinstance(field_type, String):
                if not filter_['values']:
                    logger.info(f'Invalid filter value : {filter_["values"]}')
                    continue

                if filter_['operator'] == 'starts_with':
                    q = q.filter(
                        or_(
                            *[filter_attr.ilike(v+'%') for v in filter_['values']]
                        )
                    )
                elif filter_['operator'] == 'ends_with':
                    q = q.filter(
                        or_(
                            *[filter_attr.ilike('%'+v) for v in filter_['values']]
                        )
                    )
                elif filter_['operator'] == 'contains':
                    q = q.filter(
                        or_(
                            *[filter_attr.ilike('%'+v+'%') for v in filter_['values']]
                        )
                    )
                elif filter_['operator'] == 'equals':
                    q = q.filter(
                        or_(
                            *[func.lower(filter_attr) == v.lower() for v in filter_['values']]
                        )
                    )
                elif filter_['operator'] == 'contains_sequence':
                    values = []
                    for each_value in filter_['values']:
                        filter_string = '%'
                        for each_character in each_value:
                            filter_string += f'{each_character}%'
                        values.append(filter_string)
                    filter_['values'] = values
                    q = q.filter(
                        or_(
                            *[filter_attr.ilike(v) for v in filter_['values']]
                        )
                    )
                else:
                    logger.info(
                        f'Ignoring invalid operator : {filter_["operator"]}'
                    )
            elif isinstance(field_type, Integer):
                filter_['values'] = [
                    int(v) for v in filter_['values']
                    if v and v.isdigit()
                ]

                if not filter_['values']:
                    logger.info(f'Invalid filter value : {filter_["values"]}')
                    continue

                if filter_['operator'] == 'lesser_than':
                    q = q.filter(
                        or_(*[
                            (filter_attr < v for v in filter_['values']),
                        ])
                    )
                elif filter_['operator'] == 'greater_than':
                    q = q.filter(
                        or_(*[
                            (filter_attr > v for v in filter_['values']),
                        ])
                    )
                elif filter_['operator'] == 'equals':
                    q = q.filter(
                        or_(*[
                            (filter_attr == v for v in filter_['values']),
                        ])
                    )
                elif filter_['operator'] == 'in':
                    q = q.filter(
                        or_(
                            *[filter_attr.in_(filter_['values'])]
                        )
                    )
                elif filter_['operator'] == 'not_in':
                    q = q.filter(
                        or_(
                            *[filter_attr.not_in(filter_['values'])]
                        )
                    )
                else:
                    logger.info(
                        f'Ignoring invalid operator : {filter_["operator"]}'
                    )
            elif isinstance(field_type, Date):
                filter_['values'] = [
                    v for v in filter_['values']
                    if v and is_valid_date(v)
                ]

                if not filter_['values']:
                    logger.info(f'Invalid filter value : {filter_["values"]}')
                    continue

                if filter_['operator'] == 'from':
                    q = q.filter(
                        or_(*[
                            filter_attr >= v for v in filter_['values']
                        ])
                    )
                elif filter_['operator'] == 'to':
                    q = q.filter(
                        or_(*[
                            filter_attr <= v for v in filter_['values']
                        ])
                    )
                elif filter_['operator'] == 'equals':
                    q = q.filter(
                        or_(*[
                            filter_attr == v for v in filter_['values']
                        ])
                    )
                elif filter_['operator'] == 'not_in':
                    q = q.filter(
                        or_(
                            *[filter_attr.not_in(filter_['values'])]
                        )
                    )
                else:
                    logger.info(
                        f'Ignoring invalid operator : {filter_["operator"]}'
                    )
            elif isinstance(field_type, DateTime):
                filter_['values'] = [
                    v for v in filter_['values']
                    if v and is_valid_datetime(v)
                ]

                if not filter_['values']:
                    logger.info(f'Invalid filter value : {filter_["values"]}')
                    continue

                if filter_['operator'] == 'from':
                    q = q.filter(
                        or_(*[
                            filter_attr >= v for v in filter_['values']
                        ])
                    )
                elif filter_['operator'] == 'to':
                    q = q.filter(
                        or_(*[
                            filter_attr <= v for v in filter_['values']
                        ])
                    )
                elif filter_['operator'] == 'equals':
                    q = q.filter(
                        or_(*[
                            filter_attr == v for v in filter_['values']
                        ])
                    )
                else:
                    logger.warn(
                        f'Ignoring invalid operator : {filter_["operator"]}'
                    )
            elif isinstance(field_type, Boolean):
                boolean_values = {
                    'true': True,
                    'false': False,
                    'null': None,
                }
                filter_['values'] = [
                    boolean_values[v] for v in filter_['values']
                    if v and v in boolean_values
                ]

                if not filter_['values']:
                    logger.info(f'Invalid filter value : {filter_["values"]}')
                    continue

                q = q.filter(
                    or_(*[
                        (filter_attr == v for v in filter_['values']),
                    ])
                )
            else:
                logger.warn(f'Invalid column type : {filter_["key"]}')

        return q

    @classmethod
    def apply_q_string_filter_to_query(cls, q, q_string):
        if not q_string:
            return q

        # 0. Generate the wildcard q_string
        q_wildcard_string = '%'
        for character in q_string:
            q_wildcard_string += character + '%'

        # 1. Get all searchable fields of the model
        fields = []
        for searchable_field_string in cls.searchable_fields:
            fields.append(getattr(cls, searchable_field_string))

        # 2. Loop through them and apply the search filter
        q = q.filter(
            or_(
                *[field.ilike(q_wildcard_string) for field in fields]
            )
        )

        return q

    # NOTE: Doesn't do any joins
    @classmethod
    def get_one(cls, id_or_token, with_organization=True):
        """
        Returns the object from the database based on whether the
        filter is the id or the token. Returns None if the object
        is not found.
        """
        
        filters = {}
        if with_organization and request and request.user and request.user.id_organization:
            filters['id_organization'] = request.user.id_organization

        # id_or_token contains the id
        if type(id_or_token) == int:
            filters['id_'] = id_or_token
            obj = cls.query.filter_by(**filters).first()

        # id_or_token contains the token
        elif type(id_or_token) == str:
            filters['token'] = id_or_token
            obj = cls.query.filter_by(**filters).first()

        else:
            obj = None

        return obj if obj and obj.is_deleted == False else None

    # NOTE: Doesn't do any joins
    @classmethod
    def filter_objects_by_keywords(cls, filters={}, first_one=False, with_organization=True):
        if 'is_deleted' not in filters:
            filters['is_deleted'] = False
        if with_organization and request and request.user and request.user.id_organization:
            filters['id_organization'] = request.user.id_organization

        try:
            if first_one:
                objects = cls.query.filter_by(**filters).first()
            else:
                objects = cls.query.filter_by(**filters).all()
        except Exception as e:
            logger.info(f'An exception was raised, while filtering objects by keyword')
            logger.debug(e)
            objects = None if first_one else []

        return objects

    # NOTE: Doesn't do any joins
    @classmethod
    def filter_objects_by_list_values(cls, column_, values=[], with_organization=True):
        if not column_:
            logger.info(f'Not a valid value for column')
            return None


        filters = {'is_deleted' : False}
        if with_organization and request and request.user and request.user.id_organization:
            filters['id_organization'] = request.user.id_organization

        try:
            objects = cls.query.filter_by(
                **filters
            )
            objects = objects.filter(
                column_.in_(values)
            ).all()
        except Exception as e:
            logger.info(f'An exception was raised, while filtering objects by list values')
            logger.debug(e)
            objects = []

        return objects

    # NOTE: Doesn't do any joins
    @classmethod
    def get_all(cls, with_organization=True):
        """
        Returns all the objects from the database.
        """
        filters = {'is_deleted' : False}
        if with_organization and request and request.user and request.user.id_organization:
            filters['id_organization'] = request.user.id_organization

        return cls.query.filter_by(**filters).all()

    # TODO: Accept multiple statuses
    @classmethod
    def get_all_objects(
        cls, params={}, outerjoins=[], filterable_and_sortable_fields={},
        with_organization=True,
    ):
        filters = {'is_deleted' : False}
        if with_organization and request and request.user and request.user.id_organization:
            filters['id_organization'] = request.user.id_organization

        q = cls.query.filter_by(**filters).add_entity(cls)

        # Do all necessary outerjoins
        # Joins in here must be of relation of 1 * 1
        for each_join in outerjoins:
            if len(each_join) == 3:
                q = (
                    q.outerjoin(
                        each_join[0],
                        and_(
                            each_join[1] == each_join[2],
                            each_join[0].is_deleted == False
                        )
                    ).add_entity(each_join[0])
                )
            if len(each_join) == 4:
                q = (
                    q.outerjoin(
                        each_join[0],
                        each_join[1] == each_join[2]
                    )
                )

        # Do any custom filtering
        q = cls.add_filters_to_query(
            q,
            params,
            filterable_and_sortable_fields
        )

        # Add ordering to query
        q = cls.add_ordering_to_query(
            q,
            filterable_and_sortable_fields,
            reverse=params.get('reverse', 'false'),
            order_by=params.get('order_by'),
        )

        return q

    # TODO: Accept multiple statuses
    @classmethod
    def get_all_objects_details(cls, joins=[], filters_map={}, status=None, pagination={}, is_deleted=False):
        """
        Pass status=None if you don't want the status filter to be
        applied.
        """

        # Do the status filtering
        if status is None:
            q = cls.query
        else:
            q = cls.query.filter(cls.status==status)

        if is_deleted is None:
            q = q.filter(cls.is_deleted==False)
        else:
            q = q.filter(cls.is_deleted==is_deleted)
        

        # Do any custom filtering
        q = cls.add_filters_to_query(q, filters_map, [])

        # Do all necessary joins
        for join in joins:
            q = (
                q.outerjoin(join[0], getattr(cls, join[1]) == join[0].id_)
                .add_entity(join[0])
            )

        # Do the default ordering (using the `id` field)
        q = q.order_by(
            cls.id_,
        )

        # Get the total retrieved results
        count = q.count()

        # Get paginated_query
        (q, page, page_size) = cls.add_pagination_to_query(
            q=q,
            params={
                'page': pagination.get('page'),
                'page_size': pagination.get('page_size'),
            },
        )
        
        # Fetch the results
        results = q.all()

        objects_details = []
        for result in results:
            # If not joined, `result` represents the object else,
            # need to get the details via the attribute in the
            # result object
            if len(joins) > 0:
                details = getattr(result, cls.__name__).get_details()
            else:
                details = result.get_details()

            for join in joins:
                details[join[2]] = getattr(result, join[0].__name__).get_details()
            objects_details.append(details)

        # If the `with_summary` param is set, return the data with the
        # pagination details
        if pagination.get('with_summary'):
            return (objects_details, count)

        return objects_details

    @staticmethod
    def add_ordering_to_query(q, allowed_fields, order_by=None, reverse=False):
        """
        Function to add sorting to the given query

        :param q str: Constructed query
        :param sortable_fields dict: Map of fields allowed for sorting
        :param order_by str: Order by field
        :param reverse bool: Flag to decide whether to sort ascending or descending

        :return str: Constructed query
        """

        try:
            if reverse.lower() == 'true':
                reverse = True
            else:
                reverse = False
        except (TypeError, ValueError, AttributeError):
            reverse = False

        if order_by:
            if order_by in allowed_fields:
                logger.info(f'Order by field : {order_by}')
                param = allowed_fields[order_by]

                if reverse:
                    param = desc(param)

                q = q.order_by(param)
            else:
                logger.info(f'Invalid value for order by : {order_by}')

        return q

    @staticmethod
    def add_pagination_to_query(q, params):
        """
        This function is to add pagination related clauses to the
        given query.

        :param q str: Constructed query
        :param page int: Page number
        :param page_size int: Page size

        :return str: Constructed query
        """

        # Print the query
        # print('query :', str(q.statement.compile(
        #     dialect=postgresql.dialect(),
        #     compile_kwargs={"literal_binds": True}
        # )))
        # logger.info(f'Number of records found : {q.count()}')

        if params.get('page') and params['page'].isdigit():
            page = int(params['page']) if int(params['page']) >= 1 else 0
        else:
            page = 0

        if params.get('page_size') and params['page_size'].isdigit():
            page_size = int(params['page_size']) if int(params['page_size']) >= 1 else 100
        else:
            page_size = 100

        # If page is 0, do not apply pagination
        if not page:
            return (q, page, page_size)

        # If page is valid, do pagination.
        q = (
            q.limit(page_size)
            .offset((page-1) * page_size)
        )

        return (q, page, page_size)

    @classmethod
    def return_with_summary(cls, objects=[], page=1, page_size=100, count=0):
        if page:
            total_pages = int(math.ceil(count/page_size))
            # Current page, standard page size, total pages
            pagination = (page, page_size, total_pages)
        else:
            pagination = None

        return (objects, pagination, (count,))

    # NOTE: This doesn't do any joins
    def get_details(self):
        base_details = self._get_base_details()
        main_details = self.main_details()

        return {**base_details, **main_details}

    def main_details(self):
        main_details = {}
        for field in self.readable_fields:
            try:
                getattr(self, field)
                field_type = type(self).__table__.c[field].type
            except Exception:
                logger.info(f'{type(self).__name__} Model has Invalid key in readable fields : {field}')
                continue
            if isinstance(field_type, DateTime):
                main_details[field] = serialize_datetime(getattr(self, field), datetime_format)
            elif isinstance(field_type, Date):
                main_details[field] = serialize_datetime(getattr(self, field), date_format)
            elif isinstance(field_type, Time):
                main_details[field] = serialize_datetime(getattr(self, field), time_format)
            elif isinstance(field_type, Numeric):
                main_details[field] = float(getattr(self, field)) if getattr(self, field) else None
            else:
                main_details[field] = getattr(self, field)

        return main_details


    def update(self, data, update_time=True):
        """
        This function directly updates all the elements in the `data`
        dictionary by copying their values into the corresponding
        object attribute with the same key name. All validations have
        to be take care of properly beforehand.
        """

        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                logger.info(f'{type(self).__name__} Model has no attribute : {key}')

        if update_time:
            self.last_updated_at = datetime.datetime.now(datetime.timezone.utc)

        if request and request.user and request.user.id_:
            self.id_last_updated_user = request.user.id_

        db.session.flush()

        return self

    def soft_delete(self):
        """
        This function sets the status of an object (row) to `deleted`
        and sets the value of the `deleted_at` to the current time.
        This function does not commit the changes to the database,
        that has to be taken care of in the actions layer.

        Only currently `active` objects can be deleted.
        """

        self.is_deleted = True
        self.deleted_data = self.get_details()
        self.token = None
        self.deleted_at = datetime.datetime.now(datetime.timezone.utc)

        if request and request.user and request.user.id_:
            self.id_deleted_user = request.user.id_

        db.session.flush()

        return self

    @staticmethod
    def convert_filters_to_ands_and_ors(join, model_string_alias_map):
        """
        Returns something like this:
       
        and_(
            or_(a==b, c==d),
            or_(e==f, g==h),
        )
        """

        ors_list = []
        # if 'filters' is present in join
        for key in join.get('filters', {}).keys():
            model_string, property_string = key.split('.')
            Model = model_string_alias_map[model_string]

            ands_list = []
            for allowed_value in join['filters'][key]:
                ands_list.append(getattr(Model, property_string)==allowed_value)

            ors_list.append(
                or_(*ands_list)
            )
        return and_(*ors_list)


    @classmethod
    def filter(
        cls,
        filters={},
        joins=[],
        bridge_joins=[],
        list_joins=[],
        order_by='id_',
        reverse_order=False,
        pagination={},
        get_details=True,
        first_item=False,
        params={},
    ):
        """
        sub_query is used to solve the pagination problem when doing
        left joins. (We're currently using that structure for all queries
        even when a join is not required - might have to fix it later if we
        notice any performance issue).

        Ref: https://stackoverflow.com/questions/15897055
        ChatGPT for SQLAlchemy version
        """

        # q = cls.query
        sub_query = db.session.query(cls.id_)

        # Filters related
        if 'is_deleted' not in filters:
            filters['is_deleted'] = False

        # q = q.filter_by(**filters)
        sub_query = sub_query.filter_by(**filters)

        if first_item:
            sub_query = sub_query.limit(1)
        else:
            # Get paginated_query
            (sub_query, page, page_size) = cls.add_pagination_to_query(
                q=sub_query,
                params={
                    'page': pagination.get('page'),
                    'page_size': pagination.get('page_size'),
                },
            )

        sub_query = sub_query.subquery('parent_subquery')
        parent_alias = aliased(cls, sub_query)

        q = db.session.query(cls).join(sub_query, cls.id_==sub_query.c.id_)
        
        # Apply filters to the actual query (from params)
        if hasattr(cls, 'filterable_fields'):
            filterable_fields = cls.filterable_fields
        else:
            filterable_fields = []
        filterable_fields_map = {}
        for filterable_field in filterable_fields:
            filterable_fields_map[filterable_field] = getattr(cls, filterable_field)

        q = cls.add_filters_to_query(q, params, filterable_fields_map)
        
        # Apply q_string filter to the query (from params)
        # TODO: Check if this requires protection from sql injection
        # or needs removal of any special character before passing down
        if 'q' in params:
            q = cls.apply_q_string_filter_to_query(q, params['q'])

        # Order by related
        if order_by:
            order_by_field = getattr(cls, order_by)
            if reverse_order:
                # ic('Reverse ordering..')
                order_by_field = desc(order_by_field)
            q = q.order_by(order_by_field)

        # NX1 joins (aka. normal joins)
        for i, join in enumerate(joins):
            # This alias is required so that if there are multiple columns
            # being joined to the same table, SQLAlchemy knows which column
            # join is which.
            # 
            # Regarding the naming of the alias, we're just using the model's
            # class name and joining it with the foreign key column, separated
            # by an underscore.
            aliased_model = aliased(join[0], name=f'{join[0].__name__}_{join[1]}')
            q = (
                q.outerjoin(aliased_model, getattr(cls, join[1])==aliased_model.id_)
                .add_entity(aliased_model)
            )

        # NXN joins - aka. Bridge joins
        # Join bridge first and then the secondary table
        #
        # Enumerating because the index is used as part of the alias name below
        # to avoid collision
        for i, join in enumerate(bridge_joins):
            secondary_model_aliased = aliased(
                join['secondary_model'],
                name=(
                    f'{join["secondary_model"].__name__}'
                    # f'_{join["bridge_primary_id"]}'
                    f'_{i}'
                ),
            )
            bridge_model_aliased = aliased(
                join['bridge_model'],
                name=(
                    f'{join["bridge_model"].__name__}'
                    # f'_{join["bridge_primary_id"]}'
                    f'_{i}'
                ),
            )
            q = (
                q.outerjoin(
                    # join['bridge_model'],
                    bridge_model_aliased,
                    and_(
                        # cls.id_==getattr(join['bridge_model'], join['bridge_primary_id']),
                        cls.id_==getattr(bridge_model_aliased, join['bridge_primary_id']),
                        or_(
                            # join['bridge_model'].is_deleted==False,
                            # join['bridge_model'].is_deleted==None,
                            bridge_model_aliased.is_deleted==False,
                            bridge_model_aliased.is_deleted==None,
                        ),
                        
                        # Custom join conditions. Need to do the same for
                        # joins and list joins
                        cls.convert_filters_to_ands_and_ors(
                            join=join,
                            # Passing the aliased model, because that's
                            # what should be used instead of the actual
                            # model names
                            model_string_alias_map={
                                'bridge_model': bridge_model_aliased,
                                'secondary_model': secondary_model_aliased,
                            },
                        ),
                        
                        # or_(
                        #     MetadataObjectTypeRelationship.type_=='1xn',
                        # ),
                    )
                )
                .outerjoin(
                    # join['secondary_model'],
                    secondary_model_aliased,
                    getattr(
                        bridge_model_aliased,
                        join['bridge_secondary_id']
                    # )==join['secondary_model'].id_,
                    )==secondary_model_aliased.id_,
                )
                .add_entity(bridge_model_aliased)
                # .add_entity(join['secondary_model'])
                .add_entity(secondary_model_aliased)
            )

        # 1XN joins (aka. list joins)
        for i, join in enumerate(list_joins):
            secondary_model_aliased = aliased(
                join['secondary_model'],
                name=f'{join["secondary_model"].__name__}_{i}',
            )
            # TODO: We are not using alias here as it causes some error. For
            # whatever reason the alias name is not used when doing the join.
            # We need to fix it later as multiple list joins may break
            # if this isn't fixed.
            secondary_model_aliased = join['secondary_model']
            q = (
                q.outerjoin(
                    join['secondary_model'],
                    and_(
                        cls.id_==getattr(secondary_model_aliased, join['back_reference']),
                        or_(
                            secondary_model_aliased.is_deleted==False,
                            secondary_model_aliased.is_deleted==None,
                        ),
                    ),
                )
                .add_entity(secondary_model_aliased)
            )

            # Nested joins
            if 'joins' in join:
                for i, nested_join in enumerate(join['joins']):
                    q = (
                        q.outerjoin(
                            nested_join['model'],
                            and_(
                                getattr(
                                    join['secondary_model'],
                                    nested_join['reference']
                                )==nested_join['model'].id_,
                                or_(
                                    nested_join['model'].is_deleted==False,
                                    nested_join['model'].is_deleted==None,
                                ),
                            ),
                        )
                        .add_entity(nested_join['model'])
                    )

        # Fetch the results
        results = q.all()

        # ic(cls, filters, '((((((((((((((((((()))))))))))))))))))')
        if not get_details:
            return results

        # Final list
        objects_details = []

        # To avoid row duplicates due to 1xN or NxN relationship
        primary_objects_map = {}
        bridge_joins_maps = {
            'bridge_objects_maps': {},

            # This may not be needed if we want the same secondary objects
            # connected through different bridge rows
            'secondary_objects_maps': {},
        }
        for bridge_join in bridge_joins:
            # bridge_objects_maps[bridge_join_index] = []
            bridge_joins_maps['bridge_objects_maps'][bridge_join['details_list_key']] = []
            bridge_joins_maps['secondary_objects_maps'][bridge_join['details_list_key']] = []

        print(str(q))
        # Maps to avoid duplicates
        list_joins_maps = {}
        # bridge_joins_maps = {}
        for result in results:
            # If not joined, `result` represents the object else,
            # need to get the details via the attribute in the
            # result object
            if len(joins) > 0 or len(bridge_joins) > 0 or len(list_joins) > 0:
                primary_object = getattr(result, cls.__name__)
            else:
                primary_object = result

            if primary_object.id_ not in primary_objects_map:
                primary_objects_map[primary_object.id_] = primary_object.get_details()
                details = primary_objects_map[primary_object.id_]   # Helper variable

            for bridge_join_index, bridge_join in enumerate(bridge_joins):
                # Initializing the final list
                if bridge_join['details_list_key'] not in details:
                    details[bridge_join['details_list_key']] = []

                bridge_object_alias_name = (
                    f'{bridge_join["bridge_model"].__name__}'
                    # f'_{bridge_join["bridge_primary_id"]}'
                    f'_{bridge_join_index}'
                )
                bridge_object = getattr(
                    result,
                    # bridge_join['bridge_model'].__name__,
                    bridge_object_alias_name,
                )

                # Skip if there's no bridge object
                if bridge_object is None:
                    continue

                # Skip if bridge object was already part of the map
                if bridge_object.id_ in bridge_joins_maps['bridge_objects_maps']\
                        [bridge_join['details_list_key']]:
                    continue

                bridge_joins_maps['bridge_objects_maps']\
                        [bridge_join['details_list_key']].append(bridge_object.id_)

                # Secondary object was aliased in-case we were bridging
                # between the same table
                secondary_object_alias_name = (
                    f'{bridge_join["secondary_model"].__name__}'
                    # f'_{bridge_join["bridge_primary_id"]}'
                    f'_{bridge_join_index}'
                )
                secondary_object = getattr(
                    result,
                    # bridge_join['secondary_model'].__name__,
                    secondary_object_alias_name,
                )

                # Skip if there's no secondary object
                if secondary_object is None:
                    continue

                secondary_object_details = secondary_object.get_details()

                # Skip if bridge object was already part of the map
                if secondary_object.id_ in bridge_joins_maps['secondary_objects_maps']\
                        [bridge_join['details_list_key']]:
                    continue

                bridge_joins_maps['secondary_objects_maps']\
                        [bridge_join['details_list_key']].append(secondary_object.id_)

                # If bridge table row details are requested
                if 'bridge_details_key' in bridge_join:
                    secondary_object_details[
                        bridge_join['bridge_details_key']
                    ] = bridge_object.get_details()

                details[bridge_join['details_list_key']].append(
                    secondary_object_details
                )

            for list_join_index, list_join in enumerate(list_joins):
                # Initializing the map
                if list_join['details_list_key'] not in list_joins_maps:
                    list_joins_maps[list_join['details_list_key']] = []

                # Initializing the final list
                if list_join['details_list_key'] not in details:
                    details[list_join['details_list_key']] = []

                # secondary_object_alias_name = (
                #     f'{list_join["secondary_model"].__name__}'
                #     f'_{list_join_index}'
                # )
                #
                # secondary_object = getattr(
                #     result,
                #     secondary_object_alias_name,
                #     # list_join['secondary_model'].__name__,
                #     # aliased_secondary_model.__name__,
                # )

                # TODO: Alias is not being used because of an error (mentioned
                # above in more detail already)
                secondary_object = getattr(
                    result,
                    list_join['secondary_model'].__name__,
                )

                # Skip if there's no object
                if secondary_object is None:
                    continue

                # Skip if it's already part of the map
                if secondary_object.id_ in list_joins_maps[list_join['details_list_key']]:
                    continue

                # Add to the map
                list_joins_maps[list_join['details_list_key']].append(secondary_object.id_)

                # Add to the final list
                secondary_object_details = secondary_object.get_details()

                if 'joins' in list_join:
                    for nested_join in list_join['joins']:
                        nested_joined_object = getattr(
                            result,
                            nested_join['model'].__name__,
                        )
                        if not nested_joined_object:
                            continue

                        details_key = nested_join['details_key']
                        secondary_object_details[details_key] = nested_joined_object.get_details()

                details[list_join['details_list_key']].append(secondary_object_details)

            for join in joins:
                joined_object = getattr(result, f'{join[0].__name__}_{join[1]}')

                if joined_object is not None:
                    details[join[2]] = joined_object.get_details()
                else:
                    details[join[2]] = None

        for primary_id, details in primary_objects_map.items():
            objects_details.append(details)

        # If the `with_summary` param is set, return the data with the
        # pagination details
        if pagination.get('with_summary') and pagination.get('page'):
            return cls.return_with_summary(
                objects_details,
                page,
                page_size,
                cls.query.filter(cls.is_deleted==False).count(),
            )

        if first_item:
            if len(objects_details) == 0:
                return None
            return objects_details[0]

        return objects_details

