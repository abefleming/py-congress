from pydantic import BaseModel as B

class ApiResponseRequest(B):
    contentType: str
    format: str

class ApiResponsePagination(B):
    count: int
    next: str