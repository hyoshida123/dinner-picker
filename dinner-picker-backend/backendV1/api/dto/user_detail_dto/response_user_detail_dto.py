from api.dto.parent_DTO.responseDTO import ResponseDTO

class ResponseUserDetailDTO(ResponseDTO):
    def __init__(self, id, name, preferences, groups):
        self.id = id
        self.name = name
        self.preferences = preferences
        self.groups = groups