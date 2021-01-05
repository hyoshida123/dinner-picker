"""
Group Manager

@author: SangBin Cho
"""
from api.managers.model_manager.model_creator import ModelCreator
from api.model_handler.group_model_handler import GroupModelHandler
from api.model_handler.user_model_handler import UserModelHandler
from api.util.util_functions import error_if_argument_is_default
from api.util.dto_util_functions import serialize_list
from api.util.decorators import deprecated_function
from api.exceptions.api_database_exceptions \
    import \
    APIDatabaseRetrieveFailedException, \
    APIDatabaseUpdateFailedException, \
    APIDatabaseDeleteFailedException
from api.dto.group_DTO.response_group_dto import ResponseGroupDTO

class GroupManager:
    """
    Group manager handles business logic of user activities regarding groups.

    """
    groupModelHandler = GroupModelHandler
    modelCreator = ModelCreator
    userModelHandler = UserModelHandler

    def __init__(self):
        # Add dependency injection if you want to use dependencies
        self.initialize_dependencies()

    """
    Mark- Model related actions
    """

    """
    Get Group instance
    """

    def get_group_by_groupname(self, groupname):
        return self.group_model_handler.get_group_by_groupname(groupname)

    def get_group_list_by_groupname(self, groupname):
        return self.group_model_handler.get_group_list_by_groupname(groupname)

    def get_group_by_groupid(self, groupid):
        return self.group_model_handler.get_group_by_groupid(groupid)

    def get_group_list_of_user_by_username(self, username):
        group_instance_list = self.user_model_handler.get_all_group_instances_by_username(username)
        return group_instance_list

    @deprecated_function
    def get_serialized_data_of_group_list_by_username(self, username):
        """
        Currently use Rest Framework Serializer class to serialize data because our DTO API does not support
        many objects.
        :param username
        :return: serialized data that can be used for Response
        """
        group_list = self.get_group_list_of_user_by_username(username)
        serialized_data_list = serialize_list(data=group_list, Response_DTO=ResponseGroupDTO)
        return serialized_data_list

    def get_all_groups(self):
        """
        @author Hideaki Yoshida
        """
        group_list = self.group_model_handler.get_all_groups()
        return group_list

    """
    Get User instance
    """

    def get_all_users(self):
        """
        @author Hideaki Yoshida
        """
        return self.user_model_handler.get_all_users()


    def get_users_in_the_group_by_group_id(self, group_id):
        """
        @author Hideaki Yoshida
        :param: group_id
        :return:
         """
        try:
            group_instance = self.group_model_handler.get_group_by_groupid(group_id)
            user_list = self.user_model_handler.get_users_by_group_instance(group_instance)
            return user_list
        except Exception as exception:
            print("There was a problem when getting user of {} from database: \n {}".format(group_id, str(exception)))
            raise APIDatabaseRetrieveFailedException(exception)

    def get_users_in_the_group_by_group_instance(self, group_instance):
        return self.user_model_handler.get_users_by_group_instance(group_instance)


    """
    Adding group to users
    """
    def create_group_and_add_to_user_of_username(self, username="", groupname=""):
        error_if_argument_is_default("", username)
        error_if_argument_is_default("", groupname)

        user = self.user_model_handler.get_user_by_name(username)
        group = self.modelCreator.create_group_of_groupname_and_return_instance(groupname)
        self.user_model_handler.add_group_to_user(user_instance=user, group_instance=group)
        return group

    def create_group_and_add_to_user_of_userid(self, userid="", groupname=""):
        error_if_argument_is_default("", userid)
        error_if_argument_is_default("", groupname)

        user = self.user_model_handler.get_user_by_user_id(userid)
        group = self.modelCreator.create_group_of_groupname_and_return_instance(groupname)
        self.user_model_handler.add_group_to_user(user_instance=user, group_instance=group)
        return group

    def add_group_to_user_of_username(self, username="", group_instance=None):
        error_if_argument_is_default("", username)
        error_if_argument_is_default(None, group_instance)

        user = self.user_model_handler.get_user_by_name(username)
        self.user_model_handler.add_group_to_user(user_instance=user, group_instance=group_instance)

    def add_group_to_user_of_userid(self, userid="", group_instance=None):
        error_if_argument_is_default("", userid)
        error_if_argument_is_default(None, group_instance)

        user = self.user_model_handler.get_user_by_user_id(userid)
        self.user_model_handler.add_group_to_user(user_instance=user, group_instance=group_instance)

    def add_group_of_groupid_to_user_of_username(self, username="", groupid=""):
        error_if_argument_is_default("", username)
        error_if_argument_is_default("", groupid)

        group = self.group_model_handler.get_group_by_groupid(groupid)
        user = self.user_model_handler.get_user_by_name(username)
        self.user_model_handler.add_group_to_user(user_instance=user, group_instance=group)

    def add_group_of_groupid_to_user_instance(self, user_instance=None, groupid=""):
        error_if_argument_is_default(None, user_instance)
        error_if_argument_is_default("", groupid)

        group = self.group_model_handler.get_group_by_groupid(groupid)
        self.user_model_handler.add_group_to_user(user_instance=user_instance, group_instance=group)

    """
    Leave group
    """
    def user_of_username_leave_group_of_groupid(self, groupid, username):
        """

        :param groupid
        :param username
        :return: True if success. Raise an error if fails.
        """
        user = self.user_model_handler.get_user_by_name(username)
        group = self.group_model_handler.get_group_by_groupid(groupid)
        return self.user_leave_group_of_group_instance(user_instance=user, group_instance=group)

    def user_leave_group_of_groupid(self, groupid, user_instance):
        """

        :param groupid
        :param user_instance
        :return: True if success. raise an error if fails.
        """
        group = self.get_group_by_groupid(groupid)
        return self.user_model_handler.user_instance_remove_group_instance(user_instance=user_instance, group_instance=group)

    def user_leave_group_of_group_instance(self, group_instance, user_instance):
        """

        :param group_instance
        :param user_instance
        :return: True if success. raise an error if fails.
        """
        return self.user_model_handler.user_instance_remove_group_instance(user_instance=user_instance, group_instance=group_instance)

    """
    Mark- private
    """
    def initialize_dependencies(self):
        self.group_model_handler = self.groupModelHandler()
        self.user_model_handler = self.userModelHandler()