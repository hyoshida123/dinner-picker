from api.dto.parent_DTO.requestDTO import RequestDTO

class RequestCreateGroupDTO(RequestDTO):
    def __init__(self):
        self.set_fields('name')
