
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

from datetime import datetime
from fastapi import HTTPException, Request, Response
from types import MethodType
from typing import Callable, Optional, Type, Union

from itsdangerous import BadSignature, SignatureExpired, URLSafeTimedSerializer

from sesh.models.cookie import Cookie, CookiePayload, CookieType, SameSiteEnum
from sesh.models.key import KeyBase


class CookieFactory(object):
    store: dict = {}

    def __init__(
        self,
        *,
        cookie_type: CookieType,
        created_date: str,
        created_by: int,
        data_model: Union[Type[KeyBase], Type[CookiePayload]],
        description: str,
        cookie_packer: Optional[Callable] = None,
        cookie_parser: Optional[Callable] = None,
        cookie_processor: Optional[Callable] = None,
        salt: str,
        secret_key: str,
        signer: Type[URLSafeTimedSerializer],
        domain: Optional[str] = None,
        expires: Optional[Union[int, datetime]] = None,
        httponly: bool = True,
        max_age: Optional[int] = None,
        key: str,
        path: str = "/",
        samesite: SameSiteEnum = SameSiteEnum.LAX.value,
        secure: bool = True,
        value: str,
    ):
        self._cookie_type = cookie_type
        self._created_date = created_date
        self._created_by = created_by
        self._data_model = data_model
        self._description = description

        if cookie_packer or cookie_parser or cookie_processor:
            msg = "Cannot provide cookie_packer or cookie_parser or cookie_processor without providing all three."
            assert cookie_packer and cookie_parser and cookie_processor, msg
            self._cookie_packer = MethodType(cookie_packer, self)
            self._cookie_parser = MethodType(cookie_parser, self)
            self._cookie_processor = MethodType(cookie_processor, self)
        else:
            self._cookie_packer = self.default_packer
            self._cookie_parser = self.default_parser
            # NOTE: There is never a default cookie processor as these are only used for cookies that
            # do not have an associated KeyModel
            self._cookie_processor = None

        self._salt = salt
        self._secret_key = secret_key
        self._signer = signer

        self._domain = domain
        self._expires = expires
        self._httponly = httponly
        self._max_age = max_age
        self._key = key
        self._path = path
        self._samesite = samesite
        self._secure = secure
        self._value = value

        self._cookie_model = Cookie

        CookieFactory.store[key] = self

    @property
    def created_date(self):
        return self._created_date

    @property
    def created_by(self):
        return self._created_by

    @property
    def cookie_packer(self):
        return self._cookie_packer

    @property
    def cookie_parser(self):
        return self._cookie_parser

    @property
    def cookie_processor(self):
        return self._cookie_processor

    @property
    def data_model(self):
        return self._data_model

    @property
    def description(self):
        return self._description

    @property
    def salt(self):
        return self._salt

    @property
    def secret_key(self):
        return self._secret_key

    @property
    def signer(self):
        return self._signer(self.secret_key, self.salt)

    @property
    def cookie_type(self):
        return self._cookie_type

    @property
    def domain(self):
        return self._domain

    @property
    def expires(self):
        return self._expires

    @property
    def httponly(self):
        return self._httponly

    @property
    def max_age(self):
        return self._max_age

    @property
    def key(self):
        return self._key

    @property
    def path(self):
        return self._path

    @property
    def samesite(self):
        return self._samesite

    @property
    def secure(self):
        return self._secure

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    @property
    def cookie_model(self):
        return self._cookie_model

    @classmethod
    def get_cookies(cls, cookie_types: Optional[list]):
        cookie_package = {}
        data_cookies = []

        for cookie_factory in cls.store.values():
            if cookie_factory.cookie_type is CookieType.AUTH:
                cookie_package['auth'] = cookie_factory

            if not cookie_types:
                break

            if cookie_factory.cookie_type in cookie_types:
                data_cookies.append(cookie_factory)

        cookie_package['data_cookies'] = data_cookies

        return cookie_package

    def make_cookie(self) -> Cookie:
        cookie = Cookie(
            domain=self.domain,
            expires=self.expires,
            httponly=self.httponly,
            max_age=self.max_age,
            key=self.key,
            path=self.path,
            samesite=self.samesite.value,
            secure=self.secure,
            value=self.value
        )

        return cookie

    def get_cookie_payload(self, signed_payload: Union[str, bytes]) -> str:
        try:
            payload = self.signer.loads(
                    signed_payload,
                    max_age=self.max_age,
                    return_timestamp=False,
            )
        except (SignatureExpired, BadSignature):
            raise HTTPException(status_code=403, detail="Invalid session")

        return payload

    def default_packer(self, payload: CookiePayload):
        payload_string = '.'.join(
            [payload.key_id, str(payload.key_ttl), payload.data_model, *payload.remainder]
        )
        self.value = payload_string

    def default_parser(self, signed_payload: Union[str, bytes]) -> CookiePayload:
        decrypted_payload: str = self.get_cookie_payload(signed_payload)
        parts: list = decrypted_payload.split('.')
        payload: CookiePayload = CookiePayload(
            key_id=parts[0],
            key_ttl=int(parts[1]),
            data_model=parts[2],
            remainder=parts[3:]
        )

        return payload

    def pack_payload(self, payload: CookiePayload):
        self.cookie_packer(payload)  # type: ignore

    def parse_cookie(self, signed_payload: Union[str, bytes]) -> Optional[CookiePayload]:
        payload = None
        if signed_payload:
            payload = self.cookie_parser(signed_payload)  # type: ignore

        return payload

    def process_cookie(self, request: Request, response: Response, payload: CookiePayload):
        self.cookie_processor(request, response, payload)

        return

    def attach_to_response(self, response: Response) -> None:
        cookie = self.make_cookie()
        cookie.value = str(self.signer.dumps(str(self.value)))
        response.set_cookie(
            **dict(cookie)
        )

        return

    @staticmethod
    def delete_from_response(response: Response, cookie: Cookie) -> None:
        response.delete_cookie(
            key=cookie.key,
            path=cookie.path,
            domain=cookie.domain,
        )

        return
