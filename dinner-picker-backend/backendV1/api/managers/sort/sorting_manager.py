"""
Sorting Manager is an interface that has sorting functions of searching people & restaurants.

@author: SangBin Cho.
"""


class SortingManager:
    def sort_by(self, sorting_option, list_to_sort):
        if sorting_option is 'score':
            list_to_sort = self.sort_by_score(list_to_sort)
        else:
            list_to_sort = self.sort_by_score(list_to_sort)
        return list_to_sort

    def sort_by_score(self, list_to_sort):
        return sorted(list_to_sort, key=lambda element: element.score, reverse=True)