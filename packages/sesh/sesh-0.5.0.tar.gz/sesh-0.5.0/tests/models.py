
"""
sesh is a session management library for FastAPI

Copyright (C) 2024  Brian Farrell

Initial contribution to this codebase came from a fork of
https://github.com/jordanisaacs/fastapi-sessions

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Contact: brian.farrell@me.com
"""

from datetime import datetime
from typing import Optional, Self
from typing_extensions import Annotated

from email_validator import validate_email
from httpx import AsyncClient
from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from sesh.examples.models.profile import ProfileData


class UsualSuspect(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    user_id: int
    client: Optional[AsyncClient] = None
    name_first: Optional[str] = None
    name_last: Optional[str] = None
    email_label: Optional[str] = 'primary'
    email_address: Optional[str] = None
    created_at: Annotated[Optional[str], Field(validate_default=True)] = None
    updated_at: Annotated[Optional[str], Field(validate_default=True)] = None
    profile: Optional[ProfileData] = None

    @field_validator('email_address')  # type: ignore
    @classmethod
    def validate_email_address(cls, value: str) -> str:
        emailinfo = validate_email(value)
        return emailinfo.normalized

    @model_validator(mode='after')
    def default_datetime(self) -> Self:
        if not self.created_at:
            self.created_at = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        if not self.updated_at:
            self.updated_at = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        return self
