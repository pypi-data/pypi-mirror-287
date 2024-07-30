
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

from typing import AsyncGenerator, Iterator

from asgi_lifespan import LifespanManager
from fastapi import FastAPI, status
from httpx import AsyncClient
from itsdangerous import URLSafeTimedSerializer
import pytest

from sesh.backend.memmap import InMemoryStore
from sesh.backend.redis import RedisStore
from sesh.examples.config import config

from sesh.examples import api
from sesh.examples.cookies import auth_cookie_factory
from sesh.examples.main import get_app

from .models import UsualSuspect


#########################
##### Core Fixtures #####
#########################

@pytest.fixture(scope='session')
def app() -> FastAPI:
    app_under_test = get_app()

    return app_under_test


@pytest.fixture
def backend(request) -> None:
    backend_under_test = getattr(request, 'param')

    if backend_under_test == 'memmap':
        api.backend = InMemoryStore()
    if backend_under_test == 'redis':
        api.backend = RedisStore(config.redis_dsn)


@pytest.fixture
def validator() -> None:
    pass


@pytest.fixture
def signer():
    signer = URLSafeTimedSerializer(config.secret_key, salt=config.auth_cookie_salt)

    return signer


###########################
##### Client Fixtures #####
###########################

# Make requests in our tests
# @pytest_asyncio.fixture(scope='class')
@pytest.fixture(scope='class')
async def client(app: FastAPI) -> AsyncGenerator:
    # ! IMPORTANT: http://testserver is an httpx "magic" url that tells the client to query the given app instance.
    async with LifespanManager(app):
        async with AsyncClient(
            app=app,
            base_url="http://testserver",
            follow_redirects=True,
            headers={"Content-Type": "application/json"}
        ) as async_client:
            yield async_client


###########################
##### Person Fixtures #####
###########################


@pytest.fixture
def new_user():
    person = UsualSuspect(
        user_id=next(user_id),
        name_first="Stephen",
        name_last="Guest",
        email_label="home",
        email_address="shron@luxebuds.com",
    )

    return person


def gen_id() -> Iterator[int]:
    next_id = 1
    while True:
        yield next_id
        next_id += 1


user_id = gen_id()


@pytest.fixture(scope='class')
async def auth_user(app: FastAPI, client: AsyncClient) -> UsualSuspect:  # noqa
    person = UsualSuspect(
        user_id=next(user_id),
        client=client,
        name_first="David",
        name_last="Morley",
        email_label="home",
        email_address="dutchmorley@hotmail.com",
    )
    assert person.client is not None
    login_creds = person.dict(exclude={'client', 'profile'})
    res = await person.client.post(
        app.url_path_for("login"),
        json=login_creds,
        cookies=dict(**person.client.cookies),
        headers={**person.client.headers, "X-Forwarded-For": "185.211.32.67"}
    )
    assert res.status_code == status.HTTP_201_CREATED
    assert res.json() == login_creds
    assert all(key in res.cookies for key in [
        config.auth_cookie_name,
        config.profile_cookie_name,
        config.geo_cookie_name
    ])

    cookie_factory = auth_cookie_factory
    cookie = res.cookies[config.auth_cookie_name]
    cookie_payload = cookie_factory.parse_cookie(cookie)
    assert cookie_payload.key_id != ''

    return person
