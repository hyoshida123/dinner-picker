"""
Preference Manager is an interface regarding preference settings activity.

@author: SangBin Cho
"""
from api.model_handler.user_model_handler import UserModelHandler
from api.model_handler.preference_model_handler import PreferenceModelHandler


class PreferenceManager:

    userModelHandler = UserModelHandler
    preferenceModelHandler = PreferenceModelHandler

    def __init__(self):
        super().__init__()
        self.initialize_dependencies()

    def update_preference_settings_of_username_and_return_instance(self, username, update_dict):
        """
        change the settings of a user

        :type void
        :param username: name of the user
        :param update_dict: (dictionary) new preference settings data
        """
        preference_settings = self.get_preference_settings_by_username(username)
        self.preference_model_handler.update_preference_settings(preference_settings, update_dict)
        return preference_settings

    def update_preference_settings_of_userid_and_return_instance(self, userid, update_dict):
        """
        change the settings of a user

        :type void
        :param username: name of the user
        :param update_dict: (dictionary) new preference settings data
        """
        preference_settings = self.get_preference_settings_by_userid(userid)
        self.preference_model_handler.update_preference_settings(preference_settings, update_dict)
        return preference_settings

    def get_preference_settings_by_username(self, username):
        user_account = self.user_model_handler.get_user_by_name(username)
        preference_settings_id = self.user_model_handler.get_user_preference_id_by_user_instance(user_account)
        preference_settings = self.preference_model_handler.get_preference_settings_by_id(preference_settings_id)
        return preference_settings

    def get_preference_settings_by_userid(self, userid):
        user_account = self.user_model_handler.get_user_by_user_id(userid)
        preference_settings_id = self.user_model_handler.get_user_preference_id_by_user_instance(user_account)
        preference_settings = self.preference_model_handler.get_preference_settings_by_id(preference_settings_id)
        return preference_settings

    """
    Mark- private
    """
    def initialize_dependencies(self):
        self.user_model_handler = self.userModelHandler()
        self.preference_model_handler = self.preferenceModelHandler()
