# this just adds main dir to the system path to help with the imports
import prepare_tests as _

from lib.utils import find_python_version


def test_python_version():
    assert find_python_version() == "3.12"
