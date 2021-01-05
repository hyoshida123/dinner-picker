"""
DTO Factory will return the proper DTO object based on the arguments
"""

from api.dto.external_api_DTO.yelp_restaurant_dto import YelpRestaurantDTO
from api.constants.enum_constants import APIType


class DTOFactory:
    @classmethod
    def get_restaurant_dto_of(cls, api_type):
        if api_type is APIType.YELP:
            return YelpRestaurantDTO
        else:
            return YelpRestaurantDTO
