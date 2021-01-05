"""
API Manager Factory will return the proper API Manager based on the arguments
"""

from api.managers.external_api.yelp_api_data_manager import YelpAPIDataManager
from api.constants.enum_constants import APIType


class APIManagerFactory:
    @classmethod
    def get_api_manager_instance(cls, api_type):
        if api_type is APIType.YELP:
            return YelpAPIDataManager()
        else:
            return YelpAPIDataManager()