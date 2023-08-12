from python_features_lib.utils import find_python_version

py_version = find_python_version()
available_versions = ["3.8", "3.9", "3.10", "3.11"]
if py_version in available_versions:
    if py_version == "3.8":
        from python_features_lib import v3_8 as v
    elif py_version == "3.9":
        from python_features_lib import v3_9 as v
    elif py_version == "3.10":
        from python_features_lib import v3_10 as v
    elif py_version == "3.11":
        from python_features_lib import v3_11 as v
    elif py_version == "3.12":
        from python_features_lib import v3_12 as v
    else:
        pass
else:
    raise Exception(
        "The python version you are currently using is not supported")
