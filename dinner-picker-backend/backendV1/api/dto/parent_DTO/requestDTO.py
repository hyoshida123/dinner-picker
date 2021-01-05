"""
Request DTO is used to deserialize request_dict

"""
from api.dto.parent_DTO.DTO import DTO

class RequestDTO(DTO):
    def serialize(self):
        raise Exception("Serialize is not allowed for RequestDTO children classes")