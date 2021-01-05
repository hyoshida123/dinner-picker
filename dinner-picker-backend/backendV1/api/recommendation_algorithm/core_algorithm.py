"""
Core algorithm has a series of functions that are for scoring the restaurants.

"""
from api.converter.yelp_data_converter import YelpDataConverter
from api.util.decorators import prototype_function

class CoreAlgorithm:
    def __init__(self, converter=YelpDataConverter):
        self.converter = converter()

    @prototype_function(message="Fix it.")
    def get_best_location_of_group(self, group_instance):
        return "berkeley"

    @prototype_function("Fix it.")
    def get_best_radius_of_group(self, group_instance):
        return 10000

    @prototype_function("Fix it.")
    def get_best_food_type(self, group_instance):
        return "indian"

    @prototype_function("Fix it.")
    def get_scores(self, restaurant_dto, option):
        score = 0
        for word in restaurant_dto.name:
            score += ord(word)
        return score

    def set_converter(self, converter):
        self.converter = converter

