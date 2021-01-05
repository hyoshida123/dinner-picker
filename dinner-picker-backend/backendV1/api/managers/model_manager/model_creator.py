"""
ModelCreator
In charge of creating models.
"""
from api.model_handler.preference_model_handler import PreferenceModelHandler
from api.model_handler.user_model_handler import UserModelHandler
from api.model_handler.group_model_handler import GroupModelHandler

class ModelCreator:
    preference_model_handler = PreferenceModelHandler()
    user_model_handler = UserModelHandler()
    group_model_handler = GroupModelHandler()

    @classmethod
    def save_default_preference_and_return_instance(cls):
        default_preference = cls.preference_model_handler.return_default_preference()
        cls.preference_model_handler.save_preference(default_preference)
        return default_preference

    @classmethod
    def save_customized_preference_and_return_instance(cls, food_spicy=0, food_vegan=0, food_vegetarian=0, place_loud=0):
        customized_preference = cls.preference_model_handler.return_preference_with_customized_settings(
            food_spicy=food_spicy, food_vegan=food_vegan,
            food_vegetarian=food_vegetarian, place_loud=place_loud
        )
        cls.preference_model_handler.save_preference(customized_preference)
        return customized_preference

    @classmethod
    def create_user_with_default_settings_and_return_instance(cls, username):
        """
         Create a model with username and save it. Return the user_account_model instance
         TODO It should be changed as authentication becomes stronger
         :param username: name of the user
         :return user_account model instance
         """
        preference_settings = cls.save_default_preference_and_return_instance()
        user_account = cls.user_model_handler.return_user_instance_with_preference(username, preference_settings)
        cls.user_model_handler.save_user(user_account)
        return user_account

    @classmethod
    def create_group_of_groupname_and_return_instance(cls, groupname):
        return cls.group_model_handler.save_group_and_return_instance(groupname)