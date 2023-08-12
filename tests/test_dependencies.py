import prepare_tests
from lib.utils import find_python_version


def test_python_version():
    assert find_python_version() == "3.12"
