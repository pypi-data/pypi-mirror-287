
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

from typing import Optional, Union
from fastapi import HTTPException, Request, Response
from fastapi.security.base import SecurityBase

from sesh.backend.session import SessionStore
from sesh.exceptions import SessionError
from sesh.frontend.cookie import CookieFactory, CookiePayload
from sesh.models.cookie import CookieType
from sesh.models.key import KeyBase
from sesh.validators.validator import SessionValidator


class CookieValidator(SessionValidator, SecurityBase):
    def __init__(
        self,
        *,
        auth_http_exception: HTTPException,
        auto_error: bool = False,
        backend: SessionStore,
    ):
        self._auto_error = auto_error
        self._auth_http_exception = auth_http_exception
        self._auth_only = False
        self._backend = backend

    @property
    def auto_error(self) -> bool:
        return self._auto_error

    @property
    def auth_http_exception(self) -> HTTPException:
        return self._auth_http_exception

    @property
    def auth_only(self):
        return self._auth_only

    @auth_only.setter
    def auth_only(self, value):
        self._auth_only = value

    @property
    def backend(self) -> SessionStore:
        return self._backend

    async def get_state_data(
            self,
            request,
            response,
            data_cookies: list[CookieFactory]
    ) -> Optional[dict[str, KeyBase]]:
        state_data = dict()

        for cookie_factory in data_cookies:
            if str(request.url).endswith(cookie_factory.path):
                signed_payload: str = request.cookies.get(cookie_factory.key)
                payload: CookiePayload = cookie_factory.parse_cookie(signed_payload)

                if issubclass(cookie_factory.data_model, CookiePayload) and signed_payload:
                    # Cookie is a container cookie
                    cookie_factory.process_cookie(request, response, payload)
                elif signed_payload:
                    # Cookie is used to look up a session id in storage backend and return a data_model to the route
                    data = await self.backend.read(payload.key_id, cookie_factory.data_model)
                    state_data[payload.data_model] = data

        return state_data

    async def verify_session(
            self,
            request: Request,
            response: Response,
            cookie_factory: CookieFactory,
            login_route: bool
    ) -> Optional[Union[bool, dict[str, KeyBase]]]:
        """If the session exists, it is valid"""
        # TODO: Process other potential parts of AuthModel, like RBAC
        signed_payload: str = request.cookies.get(cookie_factory.key)
        validated: bool
        result = None
        if signed_payload:
            # If there is no signed_payload, then the auth cookie was not present in the request
            payload: CookiePayload = cookie_factory.parse_cookie(signed_payload)
            validated = bool(await self.backend.check_for_key(payload.key_id))
            if validated:
                await self.backend.refresh_key_ttl(payload.key_id, payload.key_ttl)
                if login_route:
                    result = await self.get_state_data(request, response, [cookie_factory])
                else:
                    result = validated
        else:
            if login_route:
                return False
            if self.auto_error:
                raise HTTPException(status_code=403, detail="Invalid session")
            else:
                raise SessionError('validator', 'No AUTH cookie found in CookieTemplate.store')

        return result

    async def __call__(
        self,
        request: Request,
        response: Response,
        cookie_types: Optional[list[CookieType]] = None,
        login_route: bool = False
    ) -> Optional[Union[bool, dict[str, KeyBase]]]:
        # Get any cookies needed for this call
        cookies = CookieFactory.get_cookies(cookie_types)
        validated = await self.verify_session(request, response, cookies['auth'], login_route)

        if self.auth_only:
            return validated

        state_data = None

        if validated or login_route:
            try:
                state_data = await self.get_state_data(request, response, cookies['data_cookies'])
            except SessionError as error:
                if self.auto_error:
                    raise HTTPException(
                        status_code=503,
                        detail="There is a problem with the session validation service."
                    )
                raise error
        return state_data
