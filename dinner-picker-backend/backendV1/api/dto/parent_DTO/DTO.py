"""
DTO class is a parent of all DTO classes. It will have a function that converts dictionary to the object.

"""

from copy import copy

class DTO:
    def deserialize(self, request):
        """
        deserialize request_dict to a DTO class
        :return: deserialized DTO instance
        """
        if not request:
            raise ValueError("Request argument is not given.")
        try:
            request_dict = request.data
        except:
            raise Exception("request does not have request.data")
        if not request_dict:
            raise ValueError("No data in the request. No reason to use deseriazation")

        return self.deserialize_dictionary(request_dict)

    def deserialize_dictionary(self, dict_data_to_deserialize):
        """
        deserialize a dictionary to a DTO class
        :return: deserialized DTO instance
        """
        if not dict_data_to_deserialize:
            raise ValueError("Request argument is not given.")

        try:
            for attribute in self.__dict__.keys():
                if attribute in dict_data_to_deserialize:
                    self.__setattr__(attribute, dict_data_to_deserialize[attribute])
                else:
                    raise AttributeError("{} does not have {} as a key".format(dict_data_to_deserialize, attribute))
        except Exception as exception:
            raise Exception(exception)
        return self

    def serialize(self, instance_to_sync=None):
        """
        serialize DTO class
        :return: serialized response_dict
        """
        response_dict = {}
        if instance_to_sync is not None:
            self.sync_with_instance(instance_to_sync)
        try:
            for attribute, value in self.__dict__.items():
                response_dict[attribute] = value
        except Exception as exception:
            raise Exception(exception.__traceback__)
        return response_dict

    def set_fields(self, *fields):
        """
        set fields of DTO
        ex) set_fields('id', 'name')

        :param fields_set: set of field name
        :return: void
        """
        for field in fields:
            if not type(field) == str:
                raise Exception("field type should be String")
            self.__setattr__(field, None)

    def sync_with_copied_instance(self, instance):
        """
        Sync attribute data with a given instance. It uses shallow copy to create a new instance
        :param instance: instance that you want to sync attributes
        :return: dto instance that is sync with a given instance.
        """
        copied_self = copy(self)
        try:
            for attribute, value in instance.__dict__.items():
                if attribute in copied_self.__dict__.keys():
                    copied_self.__setattr__(attribute, getattr(instance, attribute))
        except Exception as exception:
            raise Exception(exception)
        return copied_self

    def sync_with_instance(self, instance):
        """
        Sync attribute data with a given instance. It uses shallow copy to create a new instance
        :param instance: instance that you want to sync attributes
        :return: returns itself after syncing data.
        """
        try:
            for attribute, value in instance.__dict__.items():
                if attribute in self.__dict__.keys():
                    self.__setattr__(attribute, getattr(instance, attribute))
        except Exception as exception:
            raise Exception(exception)
        return self