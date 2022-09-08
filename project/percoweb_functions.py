import pandas as pd
import json
# import re
import requests
from requests.structures import CaseInsensitiveDict
from date.date import server, headers_login


def auth_token(server, headers_login):
    """

    :param server:
    :param headers_login:
    :return: токен
    """
    url = f"https://{server}/api/system/auth?"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    data = headers_login
    auth = requests.post(url, headers=headers, data=data)
    token_auth = json.loads(auth.text)["token"]
    return token_auth


def users(server, token, status):
    """

    :param server:
    :param token:
    :param status:
    :return:
    """
    url = f'https://{server}/api/users/staff/table?&token={token}&status={status}&rows=5000'
    resp = requests.get(url)
    return resp


def operators(server, token):
    """

    :param server:
    :param token:
    :return:
    """
    url = f'https://{server}/api/users/operators/table?&token={token}'
    resp = requests.get(url)
    return resp


def ta_schedule(server, token):
    url = f'https://{server}/api/taSchedule/table?&token={token}'
    headers = CaseInsensitiveDict()
    resp = requests.get(url)
    return resp


def ta_scheduleid(server, token, id):
    url = f'https://{server}/api/taSchedule/{id}?&token={token}'
    headers = CaseInsensitiveDict()
    resp = requests.get(url)
    return resp


token = auth_token(server, headers_login)
operator = pd.DataFrame(json.loads(operators(token).text)["rows"])
