import inspect
from datetime import UTC, datetime
from typing import TYPE_CHECKING, Any, List, Optional, Self

from pydantic import BaseModel, Field, PrivateAttr, RootModel

from nubela_api.models.profile import Profile


def utcnow():
    return datetime.now(UTC)


class ErrorResponse(BaseModel):
    code: int
    description: str
    name: str
    _parent: Optional["Response"] = PrivateAttr(None)


class Response(BaseModel):
    profile: Optional[Profile] = Field(default=None, description="Profile data")
    error: Optional[ErrorResponse] = Field(default=None, description="Error data")
    query: dict = Field(default_factory=dict)
    query_time: datetime = Field(default_factory=utcnow)
    additional_data: dict = Field(default_factory=dict)
    code: int = Field(..., description="HTTP status code")

    def __init__(self, **data):

        ## First check if this is a profile or an error
        is_profile = False
        if not "code" in data or data["code"] == 200:
            is_profile = True
            data["code"] = 200  ## nubela on success doesn't always return this
        if not "root" in data: 
            p_or_e_key = "profile" if is_profile else "error"
            root_data = data.pop(p_or_e_key, {})  
        else:
            root_data = data.pop("root", {})

        # response fields
        rfields = set(inspect.signature(Response).parameters)
        response_data = {k: v for k, v in data.items() if k in rfields}

        if is_profile:
            ## Root data is any field that is not any of Response fields or is in Profile fields
            if not root_data:
                fields = set(inspect.signature(Profile).parameters)
                root_data = {k: v for k, v in data.items() if k in fields or k not in rfields}
            root = Profile(**root_data)
            return super().__init__(profile=root, **response_data)

        else:
            ## Root data is any field that is not any of Response fields or is in Error fields
            if not root_data:
                fields = set(inspect.signature(ErrorResponse).parameters)
                root_data = {k: v for k, v in data.items() if k in fields or k not in rfields}
            root = ErrorResponse(**root_data)
            return super().__init__(error=root, **response_data)
