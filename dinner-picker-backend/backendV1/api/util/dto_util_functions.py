"""
DTO Util Functions File has all the utility functions for processing DTO.
"""
from django.db.models.query import QuerySet

from api.util.util_functions import error_if_argument_is_default
from api.third_party_libraries.logger.singleton_logger import Logger
from api.util.decorators import deprecated_function

@deprecated_function("Use the function in DTO Manager")
def serialize_list(data=None, Response_DTO=None):
    """
    Serialize list of data.
    :param data: list of dictionary or objects
    :param Response_DTO: DTO that has the corresponding form of each data.
             If your each data is dictionary you don't need to pass anything.
    :return: list of dictionary to respond
    """
    error_if_argument_is_default(None, data)
    logger = Logger()

    if (type(data) is not list or set) and (not isinstance(data, QuerySet)):
        raise ValueError("{} function can only handle list or set or QuerySet.".format(serialize_list.__name__))

    serialized_list = []
    for data_to_serialize in data:
        if type(data_to_serialize) is not dict:
            try:
                error_if_argument_is_default(None, response_DTO)
            except:
                print("data={} contains a dictionary, but the function does not get any responseDTO".format(data))
                raise ValueError("data={} contains a dictionary, but the function does not get any responseDTO".format(data))
            response_DTO = Response_DTO()
            serialized_list.append(response_DTO.serialize(instance_to_sync=data_to_serialize))

    return serialized_list