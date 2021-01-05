"""
This file contains all the useful customized decorators

"""
from rest_framework.exceptions import APIException

from api.models.user_account.user_account_model import User
from api.constants.query_param_constants import ACCESS_TOKEN
from api.exceptions.api_auth_exceptions import APIInvalidateAccessTokenException
from api.util.util_functions import is_valid_querydict
from api.util.util_functions import is_valid_bodyfield
from api.third_party_libraries.logger.singleton_logger import Logger


def access_token_required(func):
    """
    Decorator
        parses access token from request argument and verify if it is valid.

    example:
        @access_token_required
        def get(...):
            ...

    discuss: this decorator is only for api get, post, put, delete, or etc functions.
                Use it for endpoint classes' methods.
    """
    def validator(*args, **kwargs):
        # parse request argument from APIView sort of classes' methods
        logger = Logger()
        request = args[1] # args: (api class, request) kwargs: {"form":, }
        query_param_set = request.query_params

        if not is_valid_querydict(query_param_set, "access_token"):
            raise APIException("There is no access token provided")

        if ACCESS_TOKEN in query_param_set:
            access_token = query_param_set[ACCESS_TOKEN]
        else:
            raise APIException("access token is not provided although {} api requires one.".format(str(func)))

        access_token_is_not_valid: bool = User.objects.filter(name=access_token).count() == 0
        if access_token_is_not_valid:
            raise APIInvalidateAccessTokenException("access token, {}, is invalid".format(access_token))

        print("access_token validated")
        return func(*args, **kwargs)
    return validator

def required_query_params(*queries):
    """
    Decorator
        check if *queries are included in query_parameters

    example:
        @required_query_params(ACCESS_TOKEN, USERNAME, GROUPID)
        def get(...):
            ...

    discuss: this decorator is only for api get, post, put, delete, or etc functions.
                Use it for endpoint classes' methods.
    """
    def rest_method_wrapper(func):
        def validator(*args, **kwargs):
            # parse request argument from APIView sort of classes' methods
            try:
                request = args[1] # args: (api class, request) kwargs: {"form":, }
            except:
                raise Exception("This decorator should be used only for endpoint functions")
            query_param_set = request.query_params

            if not is_valid_querydict(query_param_set, queries):
                exception_message = \
                    "actual query params: {}, required query params: {}".format(query_param_set.keys(), queries)
                raise APIException(exception_message)
            return func(*args, **kwargs)
        return validator
    return rest_method_wrapper

def required_body_field(*body_fields):
    """
    Decorator
        check if *queries are included in query_parameters

    example:
        @required_body_field(NAME, ID)
        def get(...):
            ...

    discuss: this decorator is only for api get, post, put, delete, or etc functions.
                Use it for endpoint classes' methods.
    """
    def rest_method_wrapper(func):
        def validator(*args, **kwargs):
            # parse request argument from APIView sort of classes' methods
            try:
                request = args[1] # args: (api class, request) kwargs: {"form":, }
            except:
                raise Exception("This decorator should be used only for endpoint functions")
            body_data = request.data

            if not is_valid_bodyfield(body_data, body_fields):
                exception_message = \
                    "actual body field: {}, \nrequired body field: {}".format(body_data, body_fields)
                raise APIException(exception_message)
            return func(*args, **kwargs)
        return validator
    return rest_method_wrapper


# this two higher order function is to have message as an argument of decorator
def deprecated_function(message):
    """
    Mark a function as deprecated. It will break the program if deprecated functions are used.

    @see No examples yet
    :param message: message you want to show when a deprecated function is used.
    """
    def deprecated_function_wrapper(func):
        def deprecated_function_wrapper_wrapper(*args, **kwargs):
            raise Exception("{} is deprecated".format(func.__name__))
        return deprecated_function_wrapper_wrapper
    return deprecated_function_wrapper


# this two higher order function is to have message as an argument of decorator
def deprecated_class(message):
    """
    Mark a class as deprecated. It will break the program if deprecated classes are used.

    @see GroupSerializer
    :param message: message you want to show when a deprecated class is used.
    """
    def deprecated_class_wrapper(cls):
        class DeprecatedClassWrapper:
            def __init__(self, *args, **kwargs):
                raise Exception("{} is deprecated class. {}".format(cls.__name__, message))

            def __getattr__(self, item):
                raise Exception("{} is deprecated class. {}".format(cls.__name__, message))

            def __setattr__(self, key, value):
                raise Exception("{} is deprecated class. {}".format(cls.__name__, message))

            def __call__(self, *args, **kwargs):
                raise Exception("{} is deprecated class. {}".format(cls.__name__, message))

            def __repr__(self):
                raise Exception("{} is deprecated class. {}".format(cls.__name__, message))

        return DeprecatedClassWrapper
    return deprecated_class_wrapper


def prototype_function(message=""):
    """
    Mark a function as a prototype function. It will warn developers that the function is a prototype in log messages.
    :param message: message you want to write.
    :return: void
    """
    def prototype_function_wrapper(func):
        def prototype_argument_wrapper(*args, **kwargs):
            print("{} is a prototype function. Please remove it.: {}".format(func.__name__, message))
            return func(*args, **kwargs)
        return prototype_argument_wrapper
    return prototype_function_wrapper
