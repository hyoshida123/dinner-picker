"""
Suggestion Manager is an interface for /suggestion/* endpoint.

@author: SangBin Cho
"""
from api.managers.dto.dto_manager import DTOManager
from api.managers.sort.sorting_manager import SortingManager
from api.recommendation_algorithm.core_algorithm import CoreAlgorithm
from api.model_handler.group_model_handler import GroupModelHandler
from api.models.option.suggestion_option import SuggestionOption
from api.factories.converter_factory import ConverterFactory
from api.factories.api_manager_factory import APIManagerFactory
from api.factories.dto_factory import DTOFactory
from api.util.decorators import prototype_function
from api.constants.enum_constants import APIType, SortingOption

class SuggestionManager:
    groupModelHandler = GroupModelHandler
    dtoManager = DTOManager
    coreAlgorithm = CoreAlgorithm
    sortingManager = SortingManager

    def __init__(self):
        self.initialize_dependencies()

    @prototype_function(message="It is not completed yet.")
    def get_restaurant_suggestions_of_group(self, groupid, api_type=APIType.YELP, option=None):
        """
        It needs some improvement.
        Improvement point
            1. flexible to default preference & custom preference

        :param groupid: groupid
        :param api_type: Api type that you want to get the restaurant list. Default is Yelp
        :param option: option class -> api.models.option.suggestion_option.SuggestionOption
        :return: list of restaurant objects or dictionary (need to think TODO)
        """
        APIType.validate(api_type)

        converter = ConverterFactory.get_converter_instance_of(api_type)
        self.core_algorithm.set_converter(converter)

        group = self.group_model_handler.get_group_by_groupid(groupid)
        best_location = self.core_algorithm.get_best_location_of_group(group)
        best_radius = self.core_algorithm.get_best_radius_of_group(group)
        # TODO It can be multiple
        best_food_type = self.core_algorithm.get_best_food_type(group)

        api_manager = APIManagerFactory.get_api_manager_instance(api_type)
        search_results_from_api = api_manager.get_restaurant_info(best_location, radius=best_radius, term=best_food_type)
        # it is dto class, not an instance
        RestaurantDTO = DTOFactory.get_restaurant_dto_of(api_type)
        # TODO create a restaurantDTO
        restaurant_list = self.dto_manager.deserialize_dict_list(data=search_results_from_api, DTO=RestaurantDTO)

        for restaurant in restaurant_list:
            restaurant.set_score(self.core_algorithm.get_scores(restaurant, option))

        final_suggestion = self.sorting_manager.sort_by(option.sorting_option, restaurant_list[:option.max_number])

        return final_suggestion

    def get_option(self, sorting_option_string=None, max_number=20):
        """
        Get option model instance that contains given values.
        :param sorting_option_string: sorting option
        :param max_number: max number of list you would like to get
        :return: option instance
        """
        if sorting_option_string is None:
            print("sorting option string is not given. It will be a default option, score")
            sorting_option_string = 'score'

        sorting_option = SortingOption.get_type_of(sorting_option_string)
        option = SuggestionOption(sorting_option=sorting_option, max_number=max_number)
        return option

    """
    Mark - private
    """
    def initialize_dependencies(self):
        self.group_model_handler = self.groupModelHandler()
        self.dto_manager = self.dtoManager()
        self.core_algorithm = self.coreAlgorithm()
        self.sorting_manager = self.sortingManager()


