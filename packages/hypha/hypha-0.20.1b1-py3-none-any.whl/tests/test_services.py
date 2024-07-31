"""Test services."""
import pytest
import httpx

from hypha_rpc import login, connect_to_server
from . import (
    SERVER_URL,
)

# All test coroutines will be treated as marked.
pytestmark = pytest.mark.asyncio


async def test_login(fastapi_server):
    """Test login to the server."""
    async with connect_to_server(
        {"name": "test client", "server_url": SERVER_URL}
    ) as api:
        svc = await api.get_service("public/*:hypha-login")
        assert svc and callable(svc.start)

        TOKEN = "sf31df234"

        async def callback(context):
            print(f"By passing login: {context['login_url']}")
            async with httpx.AsyncClient(timeout=20.0) as client:
                resp = await client.get(context["login_url"] + "?key=" + context["key"])
                assert resp.status_code == 200, resp.text
                assert "Hypha Account" in resp.text
                assert "{{ report_url }}" not in resp.text
                assert context["report_url"] in resp.text
                resp = await client.get(
                    context["report_url"] + "?key=" + context["key"] + "&token=" + TOKEN
                )
                assert resp.status_code == 200, resp.text

        token = await login(
            {
                "server_url": SERVER_URL,
                "login_callback": callback,
                "login_timeout": 3,
            }
        )
        assert token == TOKEN
