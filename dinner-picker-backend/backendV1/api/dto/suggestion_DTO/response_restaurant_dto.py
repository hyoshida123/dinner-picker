from api.dto.parent_DTO.responseDTO import ResponseDTO

class ResponseRestaurantDTO(ResponseDTO):
    def __init__(self):
        self.set_fields(
            'score', 'rating', 'price', 'phone',
            'id', 'alias', 'is_closed',
            'categories', 'review_count', 'name',
            'url', 'coordinates', 'image_url',
            'location', 'distance', 'transactions'
        )