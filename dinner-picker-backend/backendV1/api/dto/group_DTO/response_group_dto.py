from api.dto.parent_DTO.responseDTO import ResponseDTO

class ResponseGroupDTO(ResponseDTO):
    def __init__(self):
        self.set_fields('id', 'created', 'name', 'meeting_time')