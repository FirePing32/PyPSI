import json
import requests
import os.path
import PythonPSI
import importlib.resources as pkg_resources

URL = 'https://pypi.python.org/pypi/PythonPSI/json'

def latest_version():
    data = requests.get(URL).json()
    latest_version = data['info']['version']
    return(latest_version)

def current_version():
    VERSION = pkg_resources.read_text(PythonPSI, 'about.txt')
    return VERSION
