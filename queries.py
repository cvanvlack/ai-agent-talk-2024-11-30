from pydantic import BaseModel
from typing import List

class Queries(BaseModel):
    queries: List[str]
