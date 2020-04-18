import json
import pytest
import requests

def pytest_addoption(parser):
    parser.addoption("--test_name", action="store")


@pytest.fixture(scope="module")
def test_name(request):
    return request.config.getoption("--test_name")


@pytest.fixture(scope="module")
def call_api():
    def factory(method="GET", url="http://localhost:8000"):
        with requests.session() as session:
            with session.request(method, url) as response:
                return response.content, response.status_code
    return factory
