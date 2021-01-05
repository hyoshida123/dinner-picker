"""
Group Model Handler
Discuss: In charge of group Save, Get, Delete, Update operations

@author: SangBin Cho
"""
from api.model_handler.model_handler import ModelHandler
from api.models.group.group_model import Group
from api.exceptions.api_database_exceptions \
    import APIDatabaseRetrieveFailedException
from api.util.decorators import prototype_function


class GroupModelHandler(ModelHandler):

    # TODO Don't forget to use dependency injection if you want to add dependencies
    def __init__(self):
        super().__init__()

    def return_group_instance_of_groupname(self, groupname):
        if groupname == "":
            raise ValueError("group needs its name.")
        group = Group(name=groupname)
        return group

    """  
    Mark- save object
    """
    def save_group(self, group_instance):
        self.save_object(group_instance)

    def save_group_and_return_instance(self, groupname=""):
        """
        Create a group instance, save it, and return it.
        :param groupname: name of the group
        :return: group instance
        """
        if groupname == "":
            raise ValueError("group needs its name.")
        group = Group(name=groupname)
        self.save_object(group)
        return group

    """ 
    Mark- get object
    TODO Discuss - currently get_objects functions check exception manually. I tried to create a general get_object function,
                but there was one technological issue that I could not have general named arguments. Also tried 
                decorator solution, but it causes a problem when I wanted to use self.method. We probably can have a better 
                way later.
    """
    def get_group_by_groupname(self, groupname):
        try:
            group = Group.objects.get(name=groupname)
        except Exception as exception:
            print("There was a problem when getting {} from database: \n {}".format(Group, str(exception)))
            raise APIDatabaseRetrieveFailedException(exception)
        return group

    def get_group_list_by_groupname(self, groupname):
        try:
            group_list = Group.objects.filter(name=groupname)
        except Exception as exception:
            print("There was a problem when getting {} from database: \n {}".format(Group, str(exception)))
            raise APIDatabaseRetrieveFailedException(exception)
        return group_list

    def get_group_by_groupid(self, groupid):
        try:
            group = Group.objects.get(id=groupid)
        except Exception as exception:
            print("There was a problem when getting {} from database: \n {}".format(Group, str(exception)))
            raise APIDatabaseRetrieveFailedException(exception)
        return group

    def get_all_groups(self):
        """
        @author Hideaki Yoshida
        """
        try:
            groups = Group.objects.all()
        except Exception as exception:
            print("There was a problem when getting {} from database: \n {}".format(Group, str(exception)))
            raise APIDatabaseRetrieveFailedException(exception)
        return groups

    @prototype_function
    def get_users_in_the_group_by_group_id(self, group_id):
        try:
            group = self.get_group_by_groupid(group_id)
            user_list = group.user_set.all() # This won't work. group does not have user_set attribute
        except Exception as exception:
            print("There was a problem when getting list of users from group id:{} from database: \n {}".format(group_id, str(exception)))
            raise APIDatabaseRetrieveFailedException(exception)
        return user_list

    @prototype_function
    def get_users_in_the_group_by_group_instance(self, group_instance):
        try:
            user_list = group_instance.user_set.all() # This won't work. group does not have user_set attribute
        except Exception as exception:
            print("There was a problem when getting list of users from group id:{} from database: \n {}".format(group_instance, str(exception)))
            raise APIDatabaseRetrieveFailedException(exception)
        return user_list

    """
    Mark- private
    """
    def initialize_dependencies(self):
        # currently no dependencies
        pass