
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

from fastapi import FastAPI, status

from sesh.examples.cookies import geo_cookie_factory

from .models import UsualSuspect


class TestGeo:
    async def test_login_geo_cookie(self, app: FastAPI, auth_user: UsualSuspect) -> None:
        login_creds = {
            'user_id': auth_user.user_id,
            'email_label': auth_user.email_label,
            'email_address': auth_user.email_address
        }
        assert auth_user.client is not None
        for k, v in {
            '185.211.32.67': {
                'lat': 37.33865,
                'long': -121.88542,
                'location': 'San Jose, California, United States'
            },
            '178.18.255.111': {
                'lat': 48.10425,
                'long': 11.60102,
                'location': 'Munich, Bavaria, Germany'
            }
        }.items():
            res = await auth_user.client.post(
                app.url_path_for('login'),
                json=login_creds,
                cookies=dict(**auth_user.client.cookies),
                headers={**auth_user.client.headers, 'X-Forwarded-For': f'{k}'}
            )
            signed_payload = res.cookies.get('geo')
            payload = geo_cookie_factory.parse_cookie(signed_payload)
            assert payload.lat == v['lat']
            assert payload.long == v['long']
            assert payload.location_name == v['location']
            assert res.status_code == status.HTTP_201_CREATED
