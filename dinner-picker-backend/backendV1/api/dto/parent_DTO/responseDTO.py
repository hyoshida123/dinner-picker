"""
Response DTO is used to serialize DTO class

"""
from api.dto.parent_DTO.DTO import DTO

class ResponseDTO(DTO):
    def deserialize(self, request_dict):
        raise Exception("RequestDTO cannot deserialize data")