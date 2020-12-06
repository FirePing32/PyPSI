import importlib.resources as pkg_resources

import requests

import PythonPSI

URL = "https://pypi.python.org/pypi/PythonPSI/json"


def latest_version():
    data = requests.get(URL).json()
    latest_version = data["info"]["version"]
    return latest_version


def current_version():
    VERSION = pkg_resources.read_text(PythonPSI, "about.txt")
    return VERSION
