from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.util.decorators import access_token_required
from api.managers.user_activity.suggestion.suggestion_manager import SuggestionManager
from api.managers.dto.dto_manager import DTOManager
from api.dto.suggestion_DTO.response_restaurant_dto import ResponseRestaurantDTO
from api.constants.query_param_constants import ACCESS_TOKEN, GROUPID, API_TYPE, SORTING_OPTION, MAX_NUMBER
from api.util.decorators import required_query_params
from api.util.util_functions import get_query_value_from
from api.constants.enum_constants import APIType

class Suggest(APIView):
    """
    Suggest a best restaurants based on users' default preference.

    @path: api/suggestion/suggest
    @query params
        access_token: access token of an user.
        groupid: id of the group that wants to get suggestion.
        api_type: what api you want to use. (default is yelp)
        sorting_option: @see api.constants.enum_constants.SortingOption
        max_number: max number of result you want to receive. Default is 20. Should be less than 50
    @reponse {

    }
    """
    suggestionManager = SuggestionManager
    dtoManager = DTOManager

    @access_token_required
    @required_query_params(GROUPID, API_TYPE)
    def get(self, request, format=None):
        self.initialize_dependencies()

        # TODO access_token is currently name. Should change later
        username = get_query_value_from(request, query_name=ACCESS_TOKEN)
        groupid = get_query_value_from(request, query_name=GROUPID)
        api_type_from_query = get_query_value_from(request, query_name=API_TYPE)
        sorting_option = get_query_value_from(request, query_name=SORTING_OPTION)
        max_number = get_query_value_from(request, query_name=MAX_NUMBER)

        # TODO create an option class
        option = self.suggestion_manager.get_option(sorting_option_string=sorting_option, max_number=max_number)
        # TODO currently we are using Yelp API
        suggested_restaurants_list = \
            self.suggestion_manager.get_restaurant_suggestions_of_group(
                groupid,
                api_type=APIType.get_type_of(api_type_from_query),
                option=option
            )
        serialized_restaurant_list = \
            self.dto_manager.serialize_list(
                data=suggested_restaurants_list,
                Response_DTO=ResponseRestaurantDTO
            )

        # TODO change here
        return Response(serialized_restaurant_list, status=status.HTTP_200_OK)

    """
    Mark- private
    """
    def get_api_type(self, api_type_from_query):
        if api_type_from_query == "yelp":
            return APIType.YELP
        else:
            return APIType.YELP


    def initialize_dependencies(self):
        self.suggestion_manager = self.suggestionManager()
        self.dto_manager = self.dtoManager()