from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.util.decorators import access_token_required
from api.util.decorators import required_body_field
from api.managers.user_activity.group.group_manager import GroupManager
from api.managers.model_manager.model_creator import ModelCreator
from api.managers.dto.dto_manager import DTOManager
from api.constants.query_param_constants import ACCESS_TOKEN
from api.constants.query_param_constants import GROUPID
from api.constants.body_field_constants import NAME, ID, MEETING_TIME
from api.dto.success_failure_DTO.response_success_DTO import ResponseSuccessDTO
from api.dto.group_DTO.response_group_detail_dto import ResponseGroupDetailDTO
from api.dto.group_DTO.response_group_dto import ResponseGroupDTO
from api.dto.group_DTO.request_join_group_DTO import RequestJoinGroupDTO
from api.dto.group_DTO.request_create_group_dto import RequestCreateGroupDTO
from api.dto.user_detail_dto.response_user_detail_dto import ResponseUserDetailDTO
from api.dto.user_detail_dto.response_user_dto import ResponseUserDTO
from api.dto.settings_DTO.preference_settings_DTO import PreferenceSettingsDTO
from api.util.util_functions import get_query_value_from
from api.util.util_functions import get_body_field_value_from



class ViewGroupOfUser(APIView):
    """
    View all the group in which an user has.

    @path: group/viewGroupOfUser
    @query params
        access_token: access token of an user.
    @response {

    }
    """
    groupManager = GroupManager
    dtoManager = DTOManager

    @access_token_required
    def get(self, request, format=None):
        self.initialize_dependencies()
        # TODO access_token is currently name. Should change later
        username = get_query_value_from(request, query_name=ACCESS_TOKEN)
        # TODO This should be consistent. Change it to our DTO.
        group_list = self.group_manager.get_group_list_of_user_by_username(username)
        serialize_group_list_data = self.dto_manager.serialize_list(data=group_list, Response_DTO=ResponseGroupDTO)

        return Response(serialize_group_list_data, status=status.HTTP_200_OK)

    """
    Mark- private
    """
    def initialize_dependencies(self):
        self.group_manager = self.groupManager()
        self.dto_manager = self.dtoManager()

class CreateGroup(APIView):
    """
    create a group and add it to user's group list

    @path: group/creategroup
    @query params
        access_token: access token of an user.
    @post body {
        name: name of the group,
    }
    @response {
        "success": "success",
        "message": "group dinner tomorrow is successfully added to sang"
    }
    """
    groupManager = GroupManager
    modelCreator = ModelCreator

    @access_token_required
    @required_body_field(NAME, MEETING_TIME)
    def post(self, request, format=None):
        self.initialize_dependencies()
        # TODO access_token is currently name. Should change later
        username = get_query_value_from(request, query_name=ACCESS_TOKEN)
        create_group_dto = RequestCreateGroupDTO().deserialize(request)
        group_name = create_group_dto.name
        meeting_time = get_body_field_value_from(request, body_field_name=MEETING_TIME)

        group = self.group_manager.create_group_and_add_to_user_of_username(username=username, groupname=group_name)
        # TODO change access token to username later
        response_dto = ResponseGroupDTO().sync_with_instance(group)
        return Response(response_dto.serialize(), status=status.HTTP_200_OK)

    """
    Mark- private
    """
    def initialize_dependencies(self):
        self.group_manager = self.groupManager()


class JoinGroup(APIView):
    """
    let a specified user to join the group

    @path: group/joingroup
    @query params
        access_token: access token of an user.
    @post body {
        id: group_id
    }
    @response {
        "success": "success",
        "message": "group 8 is successfully added to oscar"
    }
    """
    groupManager = GroupManager

    @access_token_required
    @required_body_field(ID)
    def post(self, request, form=None):
        self.initialize_dependencies()
        # TODO access_token is currently name. Should change later
        joinGroupDTO = RequestJoinGroupDTO().deserialize(request)
        username = get_query_value_from(request, query_name=ACCESS_TOKEN)
        groupid = joinGroupDTO.id

        self.group_manager.add_group_of_groupid_to_user_of_username(username=username, groupid=groupid)
        success_message = "group {} is successfully added to {}".format(groupid, username)
        return Response(ResponseSuccessDTO(success_message).serialize(), status=status.HTTP_200_OK)

    """
    Mark- private
    """

    def initialize_dependencies(self):
        self.group_manager = self.groupManager()

class LeaveGroup(APIView):
    """
    Leave a group of groupid

    @path: group/leavegroup
    @query params
        access_token: access token of an user.
    @post body {
        id: id of the group,
    }
    @response {

    }
    """
    groupManager = GroupManager

    @access_token_required
    @required_body_field(ID)
    def delete(self, request, format=None):
        self.initialize_dependencies()
        # TODO access_token is currently name. Should change later
        username = get_query_value_from(request, query_name=ACCESS_TOKEN)
        groupid = get_body_field_value_from(request, body_field_name=ID)
        group = self.group_manager.get_group_by_groupid(groupid)

        self.group_manager.user_of_username_leave_group_of_groupid(groupid, username)
        # TODO change access token to username later
        success_message = "group {} is successfully removed from {}".format(groupid, username)
        return Response(ResponseSuccessDTO(success_message).serialize(), status=status.HTTP_200_OK)

    """
    Mark- private
    """
    def initialize_dependencies(self):
        self.group_manager = self.groupManager()

class ListAllGroups(APIView):
    """
    List all groups.

    @author: Hideaki Yoshida
    @path: api/group/listAllGroups
    @query params
        access_token: access token of an user.
    @response {

    }
    """
    groupManager = GroupManager
    dtoManager = DTOManager

    @access_token_required
    def get(self, request, format=None):
        self.initialize_dependencies()
        group_list_data = self.group_manager.get_all_groups()
        list_of_group_dto = []
        for group_instance in group_list_data:
            user_list = self.group_manager.get_users_in_the_group_by_group_instance(group_instance)
            list_of_user_dto = []
            for user in user_list:
                group_list_by_username = self.group_manager.get_group_list_of_user_by_username(user.name)
                group_list_dto = self.dto_manager.serialize_list(data=group_list_by_username, Response_DTO=ResponseGroupDTO)
                preference_detail = user.preferences
                preference_detail_dto = PreferenceSettingsDTO().serialize(instance_to_sync=preference_detail)
                user_dto = ResponseUserDetailDTO(user.id, user.name, preference_detail_dto, group_list_dto)
                list_of_user_dto.append(user_dto.serialize())

            group_dto = ResponseGroupDetailDTO(group_instance.id, group_instance.created, group_instance.name,
                                                   list_of_user_dto)
            list_of_group_dto.append(group_dto.serialize())

        return Response(list_of_group_dto, status=status.HTTP_200_OK)

    """
    Mark- private
    """
    def initialize_dependencies(self):
        self.group_manager = self.groupManager()
        self.dto_manager = self.dtoManager()

class GetGroupsByUsername(APIView):
    """
        List all groups of a user by username.

        @author: Hideaki Yoshida
        @path: api/group/get_groups_by_username
        @query params
            access_token: access token of an user.
        @response {

        }
    """

    groupManager = GroupManager
    dtoManager = DTOManager

    @access_token_required
    def get(self, request, format=None):
        self.initialize_dependencies()
        username = get_query_value_from(request, query_name=ACCESS_TOKEN)
        group_list = self.group_manager.get_group_list_of_user_by_username(username)
        return Response(self.dto_manager.serialize_list(data=group_list, Response_DTO=ResponseGroupDTO), status=status.HTTP_200_OK)


    """
    Mark- private
    """
    def initialize_dependencies(self):
        self.group_manager = self.groupManager()
        self.dto_manager = self.dtoManager()

class ListUsersInGroup(APIView):
    """
        List all users in a group.

        @author: Hideaki Yoshida
        @path: api/group/list_users_in_group
        @query params
            access_token: access token of an user.
        @response {

        }
    """

    groupManager = GroupManager
    dtoManager = DTOManager

    @access_token_required
    def get(self, request, format=None):
        self.initialize_dependencies()
        group_id = get_query_value_from(request, query_name=GROUPID)
        user_list = self.group_manager.get_users_in_the_group_by_group_id(group_id)
        if user_list:
            return Response(self.dto_manager.serialize_list(data=user_list, Response_DTO=ResponseUserDTO), status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


    """
    Mark- private
    """
    def initialize_dependencies(self):
        self.group_manager = self.groupManager()
        self.dto_manager = self.dtoManager()
