
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
import secrets
from typing import Union

from fastapi import FastAPI, status
from httpx import AsyncClient
from itsdangerous import URLSafeTimedSerializer
import pytest

from sesh.backend.session import SessionStore
from sesh.frontend.cookie import CookieFactory
from sesh.models.cookie import CookiePayload, CookieType, SameSiteEnum

from sesh.examples.config import config
from sesh.examples.cookies import auth_cookie_factory, profile_cookie_factory
from sesh.examples.models.profile import ProfileData
from sesh.examples.models.session import SessionData

from .models import UsualSuspect


class TestAppInit:
    def test_mismatched_packer_parser(self):
        def custom_packer(factory_instance, payload: CookiePayload):  # noqa
            payload_string = '.'.join([
                payload.key_id, payload.data_model, payload.whizbang, *payload.remainder
            ])
            self.value = payload_string

        def custom_parser(factory_instance, signed_payload: Union[str, bytes]):
            decrypted_payload: str = factory_instance.get_cookie_payload(signed_payload)
            parts: list = decrypted_payload.split('.')
            payload: CookiePayload = CookiePayload(
                key_id=parts[0], data_model=parts[1], whizbang=parts[2], remainder=parts[3:]
            )

            return payload

        def custom_processor(factory_instance, payload):  # noqa
            return payload is not None

        error_msg = "Cannot provide cookie_packer or cookie_parser or cookie_processor without providing all three."

        # Test with cookie_packer but no cookie_parser or cookie_processor
        with pytest.raises(Exception) as e:
            CookieFactory(
                cookie_type=CookieType.SESSION,
                cookie_packer=custom_packer,
                created_by=1,
                created_date=datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
                data_model=SessionData,
                description='User ProfileData Cookie',
                salt='profile_cookie_1977',
                secret_key=secrets.token_hex(32),
                signer=URLSafeTimedSerializer,
                domain=None,
                expires=None,
                httponly=True,
                max_age=config.profile_session_ttl,
                key='session',
                path='/',
                samesite=SameSiteEnum.LAX,
                secure=True,
                value=''
            )
        assert str(e.value) == error_msg

        # Test with cookie_parser but no cookie_packer or cookie_processor
        with pytest.raises(Exception) as e:
            CookieFactory(
                cookie_type=CookieType.SESSION,
                cookie_parser=custom_parser,
                created_by=1,
                created_date=datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
                data_model=SessionData,
                description='User ProfileData Cookie',
                salt='profile_cookie_1977',
                secret_key=secrets.token_hex(32),
                signer=URLSafeTimedSerializer,
                domain=None,
                expires=None,
                httponly=True,
                max_age=config.profile_session_ttl,
                key='session',
                path='/',
                samesite=SameSiteEnum.LAX,
                secure=True,
                value=''
            )
        assert str(e.value) == error_msg

        # Test with cookie_processor but no cookie_packer or cookie_parser
        with pytest.raises(Exception) as e:
            CookieFactory(
                cookie_type=CookieType.SESSION,
                cookie_processor=custom_processor,
                created_by=1,
                created_date=datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
                data_model=SessionData,
                description='User ProfileData Cookie',
                salt='profile_cookie_1977',
                secret_key=secrets.token_hex(32),
                signer=URLSafeTimedSerializer,
                domain=None,
                expires=None,
                httponly=True,
                max_age=config.profile_session_ttl,
                key='session',
                path='/',
                samesite=SameSiteEnum.LAX,
                secure=True,
                value=''
            )
        assert str(e.value) == error_msg


class TestRoutesNoAuth:
    @pytest.mark.parametrize("backend", ["memmap", "redis"], indirect=True)
    async def test_login(
        self, app: FastAPI, backend: SessionStore, client: AsyncClient, new_user: UsualSuspect,
        signer: URLSafeTimedSerializer
    ) -> None:
        login_creds = new_user.model_dump(exclude_unset=True)
        res = await client.post(
            app.url_path_for("login"),
            json=login_creds,
            headers={**client.headers, "X-Forwarded-For": "185.211.32.67"}
        )
        assert res.status_code == status.HTTP_201_CREATED
        assert res.json() == login_creds

        cookie_factory = None
        for cookie_name in ['sacs', 'session']:
            if cookie_name == 'sacs':
                cookie_factory = auth_cookie_factory
            if cookie_name == 'session':
                cookie_factory = profile_cookie_factory

            cookie = res.cookies[cookie_name]
            cookie_payload = cookie_factory.parse_cookie(cookie)

            assert cookie_payload.key_id != ''

    async def test_get_profile(self, app: FastAPI, client: AsyncClient) -> None:
        res = await client.get(
            app.url_path_for("profile")
        )
        assert res.status_code == status.HTTP_403_FORBIDDEN

    async def test_update_profile(self, app: FastAPI, client: AsyncClient) -> None:
        body = {
            "favorite_color": "Blue",
            "favorite_movie_genres": [
                "Comedy",
                "Drama",
                "Thriller",
                "Classics"
            ]
        }
        res = await client.post(
            app.url_path_for("profile:update"), json=body
        )
        assert res.status_code == status.HTTP_403_FORBIDDEN

    async def test_post_content(self, app: FastAPI, client: AsyncClient) -> None:
        body = {
            "author": "boughsof.holly@outlook.com",
            "headline": "Sesh has got your back(end)!",
            "body": "Managing sessions in FastAPI is easy with Sesh."
        }
        res = await client.post(
            app.url_path_for("content:new"), json=body
        )
        assert res.status_code == status.HTTP_403_FORBIDDEN

    async def test_logout(self, app: FastAPI, client: AsyncClient) -> None:
        res = await client.delete(
            app.url_path_for("logout")
        )
        assert res.status_code == status.HTTP_403_FORBIDDEN


class TestRoutesWithAuth:
    async def test_get_profile(self, app: FastAPI, auth_user: UsualSuspect) -> None:
        assert auth_user.client is not None
        res = await auth_user.client.get(
            app.url_path_for("profile"),
            cookies=dict(**auth_user.client.cookies),
            headers={**auth_user.client.headers, "X-Forwarded-For": "185.211.32.67"}
        )
        assert res.status_code == status.HTTP_200_OK

    async def test_update_profile(self, app: FastAPI, auth_user: UsualSuspect) -> None:
        assert auth_user.client is not None
        auth_user.profile = ProfileData(
            favorite_color="blue",
            favorite_movie_genres=["Comedy", "Drama", "Thriller", "Classics"]
        )
        body = auth_user.model_dump(exclude={"client"})
        res = await auth_user.client.post(
            app.url_path_for("profile:update"),
            json=body,
            cookies=dict(**auth_user.client.cookies),
            headers={**auth_user.client.headers, "X-Forwarded-For": "185.211.32.67"}
        )
        assert res.status_code == status.HTTP_201_CREATED
        assert res.json() == auth_user.model_dump(exclude={'client'}, exclude_unset=True)

    async def test_post_content(self, app: FastAPI, auth_user: UsualSuspect) -> None:
        assert auth_user.client is not None
        body = {
            "author": "boughsof.holly@outlook.com",
            "headline": "Sesh has got your back(end)!",
            "body": "Managing sessions in FastAPI is easy with Sesh."
        }
        res = await auth_user.client.post(
            app.url_path_for("content:new"),
            json=body,
            cookies=dict(**auth_user.client.cookies),
            headers={**auth_user.client.headers, "X-Forwarded-For": "185.211.32.67"}
        )
        assert res.status_code == status.HTTP_201_CREATED

    async def test_logout(self, app: FastAPI, auth_user: UsualSuspect) -> None:
        assert auth_user.client is not None
        res = await auth_user.client.delete(
            app.url_path_for("logout"),
            cookies=dict(**auth_user.client.cookies),
            headers={**auth_user.client.headers, "X-Forwarded-For": "185.211.32.67"}
        )
        assert res.status_code == status.HTTP_204_NO_CONTENT

        # After successful logout, log back in again because we're using session-scoped fixtures
        # to keep the same event_loop and avoid those pesky event loop errors.
        login_creds = {
            "user_id": auth_user.user_id,
            "email_label": auth_user.email_label,
            "email_address": auth_user.email_address
        }

        res = await auth_user.client.post(
            app.url_path_for("login"),
            json=login_creds,
            headers={**auth_user.client.headers, "X-Forwarded-For": "185.211.32.67"}
        )
        assert res.status_code == status.HTTP_201_CREATED
