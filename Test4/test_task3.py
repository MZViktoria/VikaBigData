import pytest

import HW4.Task3


@pytest.mark.parametrize(["data"],
                         [
                             ["error: file not found"]
                         ])
def test_stderr(data, capsys):
    """
    The capsys built-in fixer provides two bits of functionality:
     it allows you to extract stdout and stderr from some code, and temporarily disables output capture.
     Let's take a look at extracting stdout and stderr.
    """
    HW4.Task3.my_precious_logger(data)
    err = capsys.readouterr()
    assert 'error: file not found' in err.err


@pytest.mark.parametrize(["data"],
                         [
                             ["Solnishko and luna"]
                         ])
def test_stderr(data, capsys):
    HW4.Task3.my_precious_logger(data)
    out = capsys.readouterr()
    assert 'Solnishko and luna' in out.out