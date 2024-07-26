from __future__ import annotations

import os
import asyncio
import logging
from typing import TYPE_CHECKING, Iterator, AsyncIterator

import pytest

from propulsionai import PropulsionAI, AsyncPropulsionAI

if TYPE_CHECKING:
    from _pytest.fixtures import FixtureRequest

pytest.register_assert_rewrite("tests.utils")

logging.getLogger("propulsionai").setLevel(logging.DEBUG)


@pytest.fixture(scope="session")
def event_loop() -> Iterator[asyncio.AbstractEventLoop]:
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

bearer_token = "My Bearer Token"


@pytest.fixture(scope="session")
def client(request: FixtureRequest) -> Iterator[PropulsionAI]:
    strict = getattr(request, "param", True)
    if not isinstance(strict, bool):
        raise TypeError(f"Unexpected fixture parameter type {type(strict)}, expected {bool}")

    with PropulsionAI(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=strict) as client:
        yield client


@pytest.fixture(scope="session")
async def async_client(request: FixtureRequest) -> AsyncIterator[AsyncPropulsionAI]:
    strict = getattr(request, "param", True)
    if not isinstance(strict, bool):
        raise TypeError(f"Unexpected fixture parameter type {type(strict)}, expected {bool}")

    async with AsyncPropulsionAI(
        base_url=base_url, bearer_token=bearer_token, _strict_response_validation=strict
    ) as client:
        yield client
