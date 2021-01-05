"""
User Model Handler
Discuss: In charge of Save, Get, Delete, Update operations of User model.

@author: SangBin Cho
"""

from api.model_handler.model_handler import ModelHandler
from api.models.user_account.user_account_model import User
from api.exceptions.api_database_exceptions \
    import \
    APIDatabaseRetrieveFailedException, \
    APIDatabaseUpdateFailedException, \
    APIDatabaseDeleteFailedException
from api.util.util_functions import error_if_argument_is_default


class UserModelHandler(ModelHandler):

    def __init__(self):
        super().__init__()
        self.initialize_dependencies()

    def return_user_instance_with_preference(self, username, preference_settings):
        user_account = User(name=username, preferences=preference_settings)
        return user_account

    """  
    Mark- save object
    """
    def save_user(self, user_instance):
        self.save_object(user_instance)
        return True

    """
    Mark- update object that uses update_object
    """

    """
    Mark- update object that does not use update_object
    """
    def add_group_to_user(self, user_instance=None, group_instance=None):
        error_if_argument_is_default(None, user_instance)
        error_if_argument_is_default(None, group_instance)

        try:
            user_instance.groups.add(group_instance)
        except Exception as exception:
            print("There was a problem when adding a group to the user (update operation): {}".format(str(exception)))
            raise APIDatabaseUpdateFailedException
        return True

    def add_group_to_user_of_username(self, username, group_instance):
        try:
            user_account = self.get_user_by_name(username)
            user_account.groups.add(group_instance)
        except Exception as exception:
            print("There was a problem when adding a group to the user (update operation): {}".format(str(exception)))
            raise APIDatabaseUpdateFailedException
        return True

    def add_group_to_user_of_user_id(self, userid, group_instance):
        try:
            user_account = self.get_user_by_user_id(userid)
            user_account.groups.add(group_instance)
        except Exception as exception:
            print("There was a problem when adding a group to the user (update operation): {}".format(str(exception)))
            raise APIDatabaseUpdateFailedException
        return True

    """ 
    Mark- get object
    TODO Discuss - currently get_objects functions check exception manually. I tried to create a general get_object function,
                but there was one technological issue that I could not have general named arguments. Also tried 
                decorator solution, but it causes a problem when I wanted to use self.method. We probably can have a better 
                way later.
    """
    def get_all_users(self):
        try:
            user_accounts = User.objects.all()
            return user_accounts
        except Exception as exception:
            print("There was a problem when getting all users from database: \n {}".format(str(exception)))
            raise APIDatabaseRetrieveFailedException(exception)

    def get_user_by_name(self, username):
        try:
            user_account = User.objects.get(name=username)
        except Exception as exception:
            print("There was a problem when getting {} from database: \n {}".format(username, str(exception)))
            raise APIDatabaseRetrieveFailedException(exception)
        return user_account

    def get_user_by_user_id(self, userid):
        try:
            user_account = User.objects.get(id=userid)
        except Exception as exception:
            print("There was a problem when getting user of {} from database: \n {}".format(userid, str(exception)))
            raise APIDatabaseRetrieveFailedException(exception)
        return user_account

    def get_users_by_group_instance(self, group_instance):
        """
        @author Hideaki Yoshida
        :param: group_instance
        :return:
        """
        try:
            user_list = User.objects.filter(groups=group_instance)
        except Exception as exception:
            print("There was a problem when getting user of {} from database: \n {}".format(group_instance, str(exception)))
            raise APIDatabaseRetrieveFailedException(exception)
        return user_list

    def get_user_preference_id_by_user_id(self, user_id):
        try:
            user_account = User.objects.get(id=user_id)
        except Exception as exception:
            print("There was a problem when getting preference id from database: \n {}".format(str(exception)))
            raise APIDatabaseRetrieveFailedException(exception)
        return self.get_user_preference_id_by_user_instance(user_account)

    def get_user_preference_id_by_user_instance(self, user_instance):
        try:
            preference_settings = user_instance.preferences.id
        except Exception as exception:
            print("There was a problem when getting preference id from database: \n {}".format(str(exception)))
            raise APIDatabaseRetrieveFailedException(exception)
        return preference_settings

    def get_all_group_instances_by_username(self, username):
        try:
            user = self.get_user_by_name(username)
            group_list = user.groups.all()
        except Exception as exception:
            print("There was a problem when getting all users from database: \n {}".format(str(exception)))
            raise APIDatabaseRetrieveFailedException(exception)
        return group_list

    """
    Mark- delete objects
    """
    def user_instance_remove_group_instance(self, user_instance=None, group_instance=None):
        error_if_argument_is_default(None, user_instance)
        error_if_argument_is_default(None, group_instance)
        try:
            user_instance.groups.remove(group_instance)
        except Exception as exception:
            print("There was a problem when removing group, {}:{} from user, {}:{}"
                  .format(group_instance.id, group_instance.name, user_instance.id, user_instance.name))
            raise APIDatabaseDeleteFailedException(exception)
        return True

    def user_id_remove_group_instance(self, userid=None, group_instance=None):
        error_if_argument_is_default(None, userid)
        error_if_argument_is_default(None, group_instance)

        user = self.get_user_by_user_id(userid)
        return self.user_instance_remove_group_instance(user_instance=user, group_instance=group_instance)

    def user_name_remove_group_instance(self, username=None, group_instance=None):
        error_if_argument_is_default(None, username)
        error_if_argument_is_default(None, group_instance)

        user = self.get_user_by_name(username)
        return self.user_instance_remove_group_instance(user_instance=user, group_instance=group_instance)

    """
    Mark- private
    """
    def initialize_dependencies(self):
        pass