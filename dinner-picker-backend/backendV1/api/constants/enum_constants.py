from enum import Enum

""" Parent enum """
class CustomEnum(Enum):
    @classmethod
    def validate(self, enum_value):
        """
        check if enum_value exists in the Enum
        :param enum_value: enum value that you want to check if it belongs to the enum class
        :return: raise an exception if it fails to validate
        """
        if enum_value not in self:
            raise AttributeError("{} does not exist in {}".format(enum_value, self.list_keys))

    @property
    def list_keys(self):
        message_list = []
        for enum_constant in self._member_map_:
            message_list.append(enum_constant)
        return ", ".join(message_list)

    @classmethod
    def get_type_of(cls, string):
        """
        Get the enum of the corresponding string
        ex) APIType.get_type_of('yelp') will return APIType.YELP

        :param string: string that you want to convert to the enum value
        :return: enum value that corresponds to a given string
        """
        if string is None:
            raise ValueError("get_enum_value function does not get a proper string value")
        return cls(string)


""" API type """
class APIType(CustomEnum):
    YELP = "yelp"
    HARDCODE = "hardcode"

""" Sorting Option """
class SortingOption(CustomEnum):
    SCORE = 'score'