from api.dto.parent_DTO.DTO import DTO
from api.constants.body_field_constants import ID, FOOD_VEGETARIAN, FOOD_VEGAN, FOOD_SPICY, PLACE_LOUD


class PreferenceSettingsDTO(DTO):
    def __init__(self):
        self.set_fields(ID, FOOD_VEGETARIAN, FOOD_VEGAN, FOOD_SPICY, PLACE_LOUD)