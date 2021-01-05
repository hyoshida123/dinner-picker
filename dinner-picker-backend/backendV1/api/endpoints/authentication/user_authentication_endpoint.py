from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models.user_account.user_account_serializer import UserAccountSerializer
from api.util.util_functions import get_query_value_from
from api.util.decorators import access_token_required
from api.util.decorators import required_query_params
from api.model_handler.user_model_handler import UserModelHandler
from api.model_handler.preference_model_handler import PreferenceModelHandler
from api.managers.user_activity.group.group_manager import GroupManager
from api.managers.dto.dto_manager import DTOManager
from api.dto.user_detail_dto.response_user_detail_dto import ResponseUserDetailDTO
from api.dto.group_DTO.response_group_dto import ResponseGroupDTO
from api.dto.settings_DTO.preference_settings_DTO import PreferenceSettingsDTO
from api.constants.query_param_constants import USERNAME, ACCESS_TOKEN
from api.managers.model_manager.model_creator import ModelCreator
from api.dto.success_failure_DTO.response_success_DTO import ResponseSuccessDTO


# Create your views here.
class GetUserList(APIView):
    """
    list all users in the database. It is for testing

    @path: api/authentication/listUsers
    @query params
        access_token
    @response {
        [
            {
                "id": 54,
                "name": "username",
                "preferences": 46,
                "groups": []
            },
            {
                "id": 55,
                "name": "sang",
                "preferences": 47,
                "groups": []
            },
        ]
    }
    """
    userModelManager = UserModelHandler

    @access_token_required
    def get(self, request, format=None):
        self.initialize_dependencies()
        user_accounts = self.user_model_manager.get_all_users()
        print("DEBUG: user accounts are succesfully retrieved")

        serializer = UserAccountSerializer(user_accounts, many=True)
        print("DEBUG: serialization is succesfully done {}".format(serializer.data))
        return Response(serializer.data, status=status.HTTP_200_OK)

    """
    Mark- private
    """
    def initialize_dependencies(self):
        self.user_model_manager = self.userModelManager()

class ShowUserDetails(APIView):
    """
        list user details in the database given a username. It is for testing

        @author: Hideaki Yoshida
        @path: api/authentication/getUserDetails
        @query params
            access_token
        @response {
            "id": 1,
            "name": "hideaki",
            "preferences": {
                "id": 1,
                "food_vegetarian": 0,
                "food_vegan": 0,
                "food_spicy": 0,
                "place_loud": 0
            },
            "groups": [
                {
                    "id": 1,
                    "created": "2018-08-06",
                    "name": "dinner tomorrow"
                },
                {
                    "id": 2,
                    "created": "2018-08-11",
                    "name": "dinner tonight!!!"
                }
            ]
        }
    """
    userModelManager = UserModelHandler
    preferenceModelManager = PreferenceModelHandler
    groupManager = GroupManager
    dtoManager = DTOManager

    @access_token_required
    def get(self, request, format=None):
        self.initialize_dependencies()
        # TODO access_token is currently name. Should change later
        username = get_query_value_from(request, query_name=ACCESS_TOKEN)
        user = self.user_model_manager.get_user_by_name(username)

        preference_detail = self.preference_model_manager.get_preference_settings_by_id(user.preferences.id)
        preference_detail_dto = PreferenceSettingsDTO().serialize(instance_to_sync=preference_detail)
        group_detail = self.group_manager.get_group_list_of_user_by_username(username)
        group_detail_dto = self.dto_manager.serialize_list(data=group_detail, Response_DTO=ResponseGroupDTO)

        response_dto = ResponseUserDetailDTO(user.id, username, preference_detail_dto, group_detail_dto)

        return Response(response_dto.serialize(), status=status.HTTP_200_OK)

    """
    Mark- private
    """
    def initialize_dependencies(self):
        self.user_model_manager = self.userModelManager()
        self.preference_model_manager = self.preferenceModelManager()
        self.group_manager = self.groupManager()
        self.dto_manager = self.dtoManager()

class Signup(APIView):
    """
    sign up users

    @path: api/authentication/signup?username=[userName]
    @query params
        username
    @response {
        "id": 55,
        "name": "sang",
        "preferences": 47,
        "groups": []
    }
    """
    modelCreator = ModelCreator
    userModelManager = UserModelHandler

    @required_query_params(USERNAME)
    def post(self, request, format=None):
        self.initialize_dependencies()
        # TODO currently username == access token change later.
        username = get_query_value_from(request, query_name=USERNAME)

        user_account = self.model_creator.create_user_with_default_settings_and_return_instance(username)

        serializer = UserAccountSerializer(user_account)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    """
    Mark- private
    """
    def initialize_dependencies(self):
        self.user_model_manager = self.userModelManager()
        self.model_creator = self.modelCreator()

class VerifyUserLoggedIn(APIView):
    """
    Verfify is access_token is valid

    @path: api/authentication/verifyUserLoggedIn
    @query params
        access_token
    @statuscode
        200: verfieid
        401: unauthorized
    @response {
        "success": "success",
        "message": "Access token (oscar) is verified"
    }
    """

    @access_token_required
    def get(self, request, format=None):
        access_token = get_query_value_from(request, query_name=ACCESS_TOKEN)
        # wrapper checks if access token is valid
        success_message = "Access token ({}) is verified".format(str(access_token))
        success_DTO = ResponseSuccessDTO(success_message)
        return Response(success_DTO.serialize(), status=status.HTTP_200_OK)
