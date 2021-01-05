from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models.preference.preference_serializer import PreferenceSettingsSerializer
from api.util.decorators import access_token_required
from api.managers.settings.preference_manager import PreferenceManager
from api.constants.query_param_constants import ACCESS_TOKEN
from api.constants.body_field_constants import FOOD_SPICY, FOOD_VEGAN, FOOD_VEGETARIAN, PLACE_LOUD
from api.util.decorators import required_body_field
from api.util.util_functions import get_query_value_from
from api.dto.settings_DTO.preference_settings_DTO import PreferenceSettingsDTO


# Create your views here.
class PreferenceSettings(APIView):
    """
    change preference settings of the user who calls this endpoint.

    @path: api/settings/preference
    @query params
        access_token: access token of an user.
    @post body {
        food_spicy: [-3 ~ 3]
        food_vegan: [-3 ~ 3]
        food_vegetarian: [-3 ~ 3]
        place_loud: [-3 ~ 3]
    }
    """
    preferenceManager = PreferenceManager

    @access_token_required
    def get(self, request, format=None):
        """
        get preference settings of an given user
        @get response {
            "id": 46,
            "food_vegetarian": 0,
            "food_vegan": 0,
            "food_spicy": 0,
            "place_loud": 0
        }
        """
        self.initialize_dependencies()
        # TODO access_token is currently name. Should change later
        username = get_query_value_from(request, query_name=ACCESS_TOKEN)
        preference_settings = self.preference_manager.get_preference_settings_by_username(username)
        preference_settings_DTO = PreferenceSettingsDTO().sync_with_instance(preference_settings)
        return Response(preference_settings_DTO.serialize(), status=status.HTTP_200_OK)

    @access_token_required
    @required_body_field(FOOD_SPICY, FOOD_VEGAN, FOOD_VEGETARIAN, PLACE_LOUD)
    def post(self, request, format=None):
        """
        change user preference settings
        @post response {
            "id": 46,
            "food_vegetarian": 2,
            "food_vegan": 1,
            "food_spicy": 1,
            "place_loud": 3
        }
        """
        self.initialize_dependencies()
        # TODO access_token is currently name. Should change later
        username = get_query_value_from(request, ACCESS_TOKEN)
        preference_update_dict = request.data

        preference_settings = \
            self.preference_manager.update_preference_settings_of_username_and_return_instance(username, preference_update_dict)
        preference_settings_dto = PreferenceSettingsDTO().sync_with_instance(preference_settings)
        return Response(preference_settings_dto.serialize(), status=status.HTTP_200_OK)

    """
    Mark- private
    """
    def initialize_dependencies(self):
        self.preference_manager = self.preferenceManager()
