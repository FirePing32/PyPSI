import json
import requests
import os.path

URL = 'https://pypi.python.org/pypi/PythonPSI/json'

def latest_version():
    data = requests.get(URL).json()
    current_version = data['info']['version']
    return(current_version)

def current_version():
    with open(os.path.join( os.getcwd(), 'about.txt' )) as a:
        VERSION = a.read()
        return VERSION
