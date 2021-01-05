from api.dto.parent_DTO.responseDTO import ResponseDTO

class ResponseSuccessDTO(ResponseDTO):
    def __init__(self, message):
        self.success = "success"
        self.message = message

