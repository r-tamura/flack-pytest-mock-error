from unittest.mock import MagicMock, Mock

import pytest
from flask import Flask
from pytest_mock import MockerFixture

import hello

app = Flask(__name__)

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
    # mock = mocker.patch("hello.request")
    # return mock

    # OK
    # RuntimeWarning: coroutine 'AsyncMockMixin._execute_mock_call' was never awaited
    # のエラーが出力される
    with app.test_request_context():
        mock = mocker.patch("hello.request")
        yield mock


def test_helloworld(flask_request_mock):
    flask_request_mock.get_json.return_value = None
    print(type(flask_request_mock.get_json))

    hello.hello_world()

    assert 1 == 1
