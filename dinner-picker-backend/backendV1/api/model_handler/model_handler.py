"""
Model Handler
Discuss: All the logic that uses django database operation should be in this model handler.
            *All the database exceptions are handled in methods here.
            Probably it will be too long to manage later, then we can create child classes like
            UserModelHandler, PreferenceSettingsModelHandler, and etc.s
"""
from django.db.models import Model

from api.exceptions.api_database_exceptions \
    import \
    APIDatabaseSaveFailedException, \
    APIDatabaseUpdateFailedException


class ModelHandler:

    # TODO Don't forget to use dependency injection if you want to add dependencies
    def __init__(self):
        pass

    """
    Mark- CRUD private
    """
    def save_object(self, obj):
        """
        Save object(Model instance) into the database.

        :type void
        :param obj: object to save
        """
        if not isinstance(obj, Model):
            raise TypeError("the object" + str(obj) + "is not a django model")
        try:
            obj.save()
        except Exception as e:
            print("There was a problem when saving {} into database: \n {}".format(str(obj), str(e)))
            # delete if fails to save
            obj.delete()
            raise APIDatabaseSaveFailedException(str(e))

    def update_object(self, obj, update_dict):
        """
        Update Model instance. It should provide a dictionary of updating_field-updating_value

        :type boid
        :param obj: object to update
        :param update_dict: key-value pairs that represent fields and values to be updated
        """
        if not isinstance(obj, Model):
            raise TypeError("the object" + str(obj) + "is not a django model")

        try:
            for field in update_dict.keys():
                obj.__setattr__(field, update_dict[field])
            obj.save()
        except Exception as e:
            print("There was a problem when updating {} at database: \n {}".format(str(obj), str(e)))
            raise APIDatabaseUpdateFailedException(str(e))

    """
    Mark- private
    """

    def initialize_dependencies(self):
        # currently no dependencies
        pass

