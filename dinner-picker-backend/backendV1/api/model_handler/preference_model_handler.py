"""
Preference Model Handler
Discuss: In charge of preference Save, Get, Delete, Update operations

@author: SangBin Cho
"""
from api.model_handler.model_handler import ModelHandler
from api.models.preference.preference_model import Preferences
from api.exceptions.api_database_exceptions \
    import APIDatabaseRetrieveFailedException


class PreferenceModelHandler(ModelHandler):
    # TODO Don't forget to use dependency injection if you want to add dependencies
    def __init__(self):
        super().__init__()

    def return_default_preference(self):
        default_preference = Preferences(food_spicy=0, food_vegan=0, food_vegetarian=0, place_loud=0)
        return default_preference

    def return_preference_with_customized_settings(self, food_spicy=0, food_vegan=0, food_vegetarian=0, place_loud=0):
        preference_settings = Preferences(food_spicy=food_spicy, food_vegan=food_vegan, food_vegetarian=food_vegetarian, place_loud=place_loud)
        return preference_settings

    """  
    Mark- save object
    """
    def save_preference(self, preference_instance):
        self.save_object(preference_instance)

    """
    Mark- update object that uses update_object
    """
    def update_preference_settings(self, preference_settings, update_dict):
        self.update_object(preference_settings, update_dict)

    def update_preference_settings_by_preference_id(self, preference_id, update_dict):
        preference_settings = self.get_preference_settings_by_id(preference_id)
        self.update_object(preference_settings, update_dict)

    """ 
    Mark- get object
    TODO Discuss - currently get_objects functions check exception manually. I tried to create a general get_object function,
                but there was one technological issue that I could not have general named arguments. Also tried 
                decorator solution, but it causes a problem when I wanted to use self.method. We probably can have a better 
                way later.
    """
    def get_preference_settings_by_id(self, preference_id):
        try:
            preference_settings = Preferences.objects.get(id=preference_id)
        except Exception as exception:
            print("There was a problem when getting {} from database: \n {}".format(Preferences, str(exception)))
            raise APIDatabaseRetrieveFailedException(exception)
        return preference_settings

    """
    Mark- private
    """
    def initialize_dependencies(self):
        pass
