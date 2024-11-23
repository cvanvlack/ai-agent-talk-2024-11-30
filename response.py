from pydantic import BaseModel

class Response(BaseModel):
    """Response to user."""

    response: str
