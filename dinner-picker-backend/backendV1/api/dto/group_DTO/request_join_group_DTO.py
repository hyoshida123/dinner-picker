from api.dto.parent_DTO.requestDTO import RequestDTO

class RequestJoinGroupDTO(RequestDTO):
    def __init__(self):
        self.set_fields('id')