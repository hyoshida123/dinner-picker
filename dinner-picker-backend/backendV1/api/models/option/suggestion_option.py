"""
SuggestionOption is the object that is used for the suggestion algorithm. It is working as a cache object.
"""
from api.constants.enum_constants import SortingOption

class SuggestionOption:
    def __init__(self, sorting_option=SortingOption.SCORE, max_number=50):
        self.sorting_option = sorting_option
        self.max_number = max_number
