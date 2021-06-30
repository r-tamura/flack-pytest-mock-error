## 環境

| 確認した環境  |
| :-----------: |
| python: 3.8.6 |

## 再現方法

このレポジトリをクローン後

### 1. flask,pytest,pytest-mock をインストール

```sh
pip install -r requirements.txt
```

### 2. テストの実行

```sh
> pytest
=================================================== test session starts ====================================================
platform darwin -- Python 3.8.6, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /Users/r-tamura/playground/python-testing-flask
plugins: mock-3.6.1
collected 1 item

test_hello.py E                                                                                                      [100%]

========================================================== ERRORS ==========================================================
____________________________________________ ERROR at setup of test_helloworld _____________________________________________

mocker = <pytest_mock.plugin.MockerFixture object at 0x1043a99d0>

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
>       mock = mocker.patch("hello.request")

test_hello.py:18:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
.venv/lib/python3.8/site-packages/pytest_mock/plugin.py:374: in __call__
    return self._start_patch(
.venv/lib/python3.8/site-packages/pytest_mock/plugin.py:183: in _start_patch
    mocked = p.start()  # type: unittest.mock.MagicMock
../../.anyenv/envs/pyenv/versions/3.8.6/lib/python3.8/unittest/mock.py:1529: in start
    result = self.__enter__()
../../.anyenv/envs/pyenv/versions/3.8.6/lib/python3.8/unittest/mock.py:1416: in __enter__
    if spec is None and _is_async_obj(original):
../../.anyenv/envs/pyenv/versions/3.8.6/lib/python3.8/unittest/mock.py:51: in _is_async_obj
    if hasattr(obj, '__func__'):
.venv/lib/python3.8/site-packages/werkzeug/local.py:422: in __get__
    obj = instance._get_current_object()
.venv/lib/python3.8/site-packages/werkzeug/local.py:544: in _get_current_object
    return self.__local()  # type: ignore
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

name = 'request'

    def _lookup_req_object(name):
        top = _request_ctx_stack.top
        if top is None:
>           raise RuntimeError(_request_ctx_err_msg)
E           RuntimeError: Working outside of request context.
E
E           This typically means that you attempted to use functionality that needed
E           an active HTTP request.  Consult the documentation on testing for
E           information about how to avoid this problem.

.venv/lib/python3.8/site-packages/flask/globals.py:33: RuntimeError
================================================= short test summary info ==================================================
ERROR test_hello.py::test_helloworld - RuntimeError: Working outside of request context.
===================================================== 1 error in 0.37s =====================================================
```
