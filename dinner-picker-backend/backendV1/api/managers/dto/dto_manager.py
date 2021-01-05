"""
DTO Manager is an interface that has useful functions about DTO.
"""
from django.db.models.query import QuerySet

from api.util.util_functions import error_if_argument_is_default
from api.third_party_libraries.logger.singleton_logger import Logger


class DTOManager:
    def serialize_list(self, data=None, Response_DTO=None):
        """
        Serialize list of data.
        :param data: list of dictionary or objects
        :param Response_DTO: DTO that has the corresponding form of each data.
                 If your each data is dictionary you don't need to pass anything.
        :return: list of dictionary to respond
        """
        error_if_argument_is_default(None, data)
        logger = Logger()

        if (type(data) is not list and set) and (not isinstance(data, QuerySet)):
            raise ValueError("{} function can only handle list or set or QuerySet.".format(self.serialize_list.__name__))

        serialized_list = []
        for data_to_serialize in data:
            if type(data_to_serialize) is not dict:
                if Response_DTO is None:
                    print("data={} contains a dictionary, but the function does not get any responseDTO".format(data))
                    raise ValueError

                response_DTO = Response_DTO()
                serialized_list.append(response_DTO.serialize(instance_to_sync=data_to_serialize))

        return serialized_list

    def deserialize_dict_list(self, data=None, DTO=None):
        """
        Deserialize list of data in a dictionary type. EX) request.data is a dictionary type.
        :param data: list of dictionary
        :param DTO: DTO that has the corresponding form of each data. It is a dto object.
        :return: list of dictionary to respond
        """
        error_if_argument_is_default(None, data)
        logger = Logger()

        if (type(data) is not list and set) and (not isinstance(data, QuerySet)):
            raise ValueError("{} function can only handle list or set or QuerySet.".format(self.deserialize_dict_list.__name__))

        deserialized_list = []
        for data_to_deserialize in data:
            if type(data_to_deserialize) is not dict:
                print("data={} is not a dictionary. It should be a dictionary to deserialize".format(data))
                raise ValueError

            deserialized_list.append(DTO().deserialize_dictionary(data_to_deserialize))

        return deserialized_list
