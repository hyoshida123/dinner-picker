"""
This file is for utility functions

"""

from api.third_party_libraries.logger.singleton_logger import Logger

def is_valid_querydict(querydict, required_queries):
    """
    Check if required_queries are in querydict.

    @param querydict: request.query_params
    @param required_query:  (String) required queries in querydict

    """
    return is_valid_values_in_dict(querydict, required_queries)

def is_valid_bodyfield(body_dict, required_body_field):
    """
    Check if required_body_field is in body dict
    :param body_dict:
    :param required_body_field:
    :return: True if valid. raise an error if not.
    """
    return is_valid_values_in_dict(body_dict, required_body_field)

def get_query_value_from(request, query_name=None):
    """
    Get query value of query_name from the request. It is only used in endpoints classes.
    :param request: request object
    :param query_name: query name you want to parse from request
    :return: value of query param of query_name. If query value does not exist, it will return None
    """
    error_if_argument_is_default(None, query_name)
    logger = Logger()
    query_sets = request.query_params
    if query_name not in query_sets:
        print("{} is not in the request.query_params {}".format(query_name, query_sets))
        return None
    return query_sets[query_name]

def get_body_field_value_from(request, body_field_name=None):
    """
    Get the value of body_field. It is only used in endpoints classes.
    :param request: request object
    :param body_field_name: body field name that you want to parse the value of it from the request
    :return: value of the body_field_name in the request
    """
    error_if_argument_is_default(None, body_field_name)
    body_data = request.data
    if body_field_name not in body_data:
        raise ValueError("{} is not in the request.data {}".format(body_field_name, body_data))
    return body_data[body_field_name]


def error_if_argument_is_default(default, arg):
    """
    Check if the argument is default. It is used for naming arugments.

    EX)
    def check_user_is_in_group(userid=None, groupid=None):
        error_if_argument_is_default(None, userid)
        error_if_argument_is_default(None, groupid)

    :param default: Default value of naming argument you want to avoid.
    :param arg: Value of argument you want to check if it is default value.
    :return: Nothing if the argument is not a default value. raise an ValueError if it is.
    """
    if not arg:
        raise ValueError("argument {} does not exist.".format(arg))
    if arg is default:
        raise ValueError("argument {} is a default value, {}. Please pass the value to it.".format(arg, default))

"""
Mark - private
"""
def is_valid_values_in_dict(dictionary, required_field):
    if type(required_field) is str:
        required_field = [required_field]
    for field in required_field:
        if field not in dictionary.keys():
            raise Exception("invalid query dict. actual: {} expected: {}".format(dictionary, required_field))
    return True
