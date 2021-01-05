"""
ConverterFactory returns a proper converter class based on the given arguments.

"""
from api.constants.enum_constants import APIType
from api.converter.yelp_data_converter import YelpDataConverter

class ConverterFactory:
    @classmethod
    def get_converter_instance_of(cls, api_type):
        if api_type is APIType.YELP:
            return YelpDataConverter()
        else:
            return YelpDataConverter()