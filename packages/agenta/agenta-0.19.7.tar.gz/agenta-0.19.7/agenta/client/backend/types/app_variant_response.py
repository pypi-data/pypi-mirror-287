# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class AppVariantResponse(pydantic.BaseModel):
    app_id: str
    app_name: str
    variant_id: str
    variant_name: str
    parameters: typing.Optional[typing.Dict[str, typing.Any]]
    previous_variant_name: typing.Optional[str]
    user_id: str
    base_name: str
    base_id: str
    config_name: str
    uri: typing.Optional[str]
    revision: int
    organization_id: typing.Optional[str]
    workspace_id: typing.Optional[str]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {
            "by_alias": True,
            "exclude_unset": True,
            **kwargs,
        }
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
