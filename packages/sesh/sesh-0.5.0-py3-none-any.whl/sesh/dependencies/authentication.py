
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

from typing import List, Tuple

from fastapi import Depends, HTTPException, Request, Response

from sesh.models.cookie import CookieType
from sesh.validators.cookie import CookieValidator


def get_request(request: Request):
    return request


def get_response(response: Response):
    return response


def login_check(validator: CookieValidator):
    async def check_auth(request=Depends(get_request), response=Depends(get_response)):
        validator.auth_only = True
        # We need to catch the exception here and then re-raise it so that
        # we can set validator.auth_only back to False in the finalizer
        try:
            state_data: dict = await validator(request, response, login_route=True)
        except HTTPException as e:
            raise e
        finally:
            validator.auth_only = False

        return state_data
    return check_auth


def user_auth(validator: CookieValidator):
    async def get_auth(request=Depends(get_request), response=Depends(get_response)):
        validator.auth_only = True
        # We need to catch the exception here and then re-raise it so that
        # we can set validator.auth_only back to False in the finalizer
        try:
            await validator(request, response)
        except HTTPException as e:
            raise e
        finally:
            validator.auth_only = False

    return get_auth


def user_session(desired_state: Tuple[CookieValidator, List[CookieType]]):
    async def get_session_data(request=Depends(get_request), response=Depends(get_response)):
        validator = desired_state[0]
        cookie_types = desired_state[1]

        state_data = await validator(request, response, cookie_types)

        return state_data
    return get_session_data
