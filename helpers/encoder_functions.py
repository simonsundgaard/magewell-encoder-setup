import requests
import json
import os
from helpers.response_codes import response_code_debug


def login(ip):
    url = "http://"+ip+"/usapi?method=login&id=Admin&pass=e3afed0047b08059d0fada10f400c1e5"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    #sid = json.loads(response.text)["sid"]

    headers = {
        "Cookie": ""
    }

    for c in response.cookies:
        headers["Cookie"] = c.name+"="+c.value
        return headers


def get_settings(ip, headers):
    url = "http://"+ip+"/usapi?method=get-settings"

    payload = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    body = json.loads(response.text)

    return response, body


def add_nosignal_file(ip, headers, filename):
    # Delete the old one first
    delete_nosignal_file(ip, headers, filename)

    url = "http://"+ip+"/usapi?method=add-nosignal-file"
    payload = {}
    filename_only = os.path.basename(filename)
    files = [('', (filename_only, open(filename, 'rb'), 'image/jpeg'))]

    response = requests.request(
        "POST", url, headers=headers, data=payload, files=files)

    os.remove(filename)
    set_nosignal_file(ip, headers)
    return response.text


def delete_nosignal_file(ip, headers, filename):
    url = "http://"+ip+"/usapi?method=del-nosignal-file&id=2"
    payload = {}

    response = requests.request(
        "GET", url, headers=headers, data=payload)
    return response.text


def set_nosignal_file(ip, headers):
    url = "http://"+ip+"/usapi?method=set-nosignal-file&id=2"
    payload = {}

    response = requests.request(
        "GET", url, headers=headers, data=payload)

    response_code_debug(response.text)

    return


if __name__ == '__main__':
    login("10.2.0.124")
