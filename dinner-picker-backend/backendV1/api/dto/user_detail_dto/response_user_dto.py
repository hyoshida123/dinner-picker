from api.dto.parent_DTO.responseDTO import ResponseDTO

class ResponseUserDTO(ResponseDTO):
    def __init__(self):
        self.set_fields('id', 'name')