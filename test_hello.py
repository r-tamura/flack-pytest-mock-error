from unittest.mock import MagicMock, Mock

import pytest
from pytest_mock import MockerFixture


@pytest.fixture
def flask_request_mock(mocker: MockerFixture) -> MagicMock:
    # OK
    # mock = Mock()
    # mocker.patch("hello.request", mock)
    # return mock

    # NG
    #
    # ERROR test_hello.py::test_helloworld - RuntimeError: Working outside of request context.
    # が発生する
    mock = mocker.patch("hello.request")
    return mock


def test_helloworld(flask_request_mock):
    assert 1 == 1
