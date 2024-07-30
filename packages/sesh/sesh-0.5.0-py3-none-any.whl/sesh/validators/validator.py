
"""
sesh is a session management library for FastAPI

Copyright (C) 2024  Brian Farrell

Initial contribution to this codebase came from a fork of
https://github.com/jordanisaacs/fastapi-sessions

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Contact: brian.farrell@me.com
"""

from abc import ABC, abstractmethod
from typing import Optional, Type

from fastapi import HTTPException, Request, Response

from sesh.backend.session import SessionStore
from sesh.frontend.cookie import CookieFactory
from sesh.models.key import KeyBase
from sesh.models.cookie import CookieType


class SessionValidator(ABC):
    @abstractmethod
    def __init__(self) -> None:
        raise NotImplementedError()

    @property
    @abstractmethod
    def auto_error(self) -> bool:
        raise NotImplementedError()

    @property
    @abstractmethod
    def auth_http_exception(self) -> HTTPException:
        raise NotImplementedError()

    @property
    @abstractmethod
    def auth_only(self):
        raise NotImplementedError()

    @auth_only.setter
    @abstractmethod
    def auth_only(self, value):
        raise NotImplementedError()

    @property
    @abstractmethod
    def backend(self) -> SessionStore:
        raise NotImplementedError()

    @abstractmethod
    async def verify_session(
            self,
            request: Request,
            response: Response,
            cookie_factory: CookieFactory,
            login_route: bool
    ) -> bool:
        raise NotImplementedError()

    @abstractmethod
    async def __call__(
        self,
        request: Request,
        response: Response,
        cookie_types: Optional[list[CookieType]] = None
    ) -> Optional[list[Type[KeyBase]]]:
        raise NotImplementedError()
