from api.dto.group_DTO.response_group_dto import ResponseGroupDTO

class ResponseGroupDetailDTO(ResponseGroupDTO):
    def __init__(self, id, created, name, users):
        self.id = id
        self.created = created
        self.name = name
        self.users = users