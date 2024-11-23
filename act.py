from typing import Annotated, List, Tuple
from pydantic import BaseModel, Field
from plan import Plan
from response import Response
from typing import Union

class Act(BaseModel):
    """Action to perform."""

    action: Union[Response, Plan] = Field(
        description="Action to perform. If you want to respond to user, use Response. "
        "If you need to further use tools to get the answer, use Plan."
    )
