from typing import Any

from pydantic import BaseModel, ConfigDict

from doip_sdk.constant import ResponseStatus


class DOIPResponse(BaseModel):
    model_config = ConfigDict(
        # So that when we serialize the model, we get the string value of the enum instead of the enum object
        use_enum_values=True
    )

    requestId: str | None = None
    status: ResponseStatus
    attributes: list = None
    output: Any | None = None
