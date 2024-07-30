from enum import Enum
import json
from httpx import Response

class ErrorCode(Enum):
    SUCCESS = (0, "Success")
    FILE_EXISTS = (1001, "File already exists")
    FILE_NOT_FOUND = (1002, "File not found")
    INVALID_FILE_SUFFIX = (1003, "Invalid file suffix")
    UNKNOWN_ERROR = (9999, "Unknown error")

    def __init__(self, code, message):
        self.code = code
        self.message = message
        
class SdmsResponse:
    def __init__(self, code=ErrorCode.SUCCESS, data=None, err_msg=None):
        self.code = code.code if isinstance(code, ErrorCode) else code    
        self.data = data or {}    
        if self.code != 0:
            if err_msg is not None:
                self.error = {"msg": err_msg}
            else:
                self.error = {"msg": code.message}
        if data is not None:
            self.data = data

    @property
    def json(self):
        response = {"code": self.code}
        if self.code == 0:
            response["data"] = self.data
        else:
            response["error"] = self.error
        return json.dumps(response)