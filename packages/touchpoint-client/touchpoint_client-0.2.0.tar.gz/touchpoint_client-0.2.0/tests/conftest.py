import pytest
from touchpoint_client import TouchpointClient
import json

with open("test/credentials.json", encoding="utf-8", mode="r") as f:
    TOUCHPOINT_CONFIG = json.load(f)


@pytest.fixture(scope="session")
def default_client():
    yield TouchpointClient(**TOUCHPOINT_CONFIG)
