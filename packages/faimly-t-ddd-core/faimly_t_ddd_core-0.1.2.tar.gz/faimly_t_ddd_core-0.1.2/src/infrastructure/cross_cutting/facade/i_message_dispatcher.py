from pydantic import BaseModel


class ResponseDispatcher(BaseModel):
    is_success: bool
    status_code: int
    response_json: str