# encoding: utf-8
from flask import json
from jsonrpc.backend.flask import api


@api.dispatcher.add_method
def login(name, pwd):
    """
    :description 登录接口
    :param name: str
    :param pwd: str
    :return: 登录信息
    """
    result = {"msg": "login success", "code": 200}
    return result


@api.dispatcher.add_method
def logout(name):
    """
    :description 退出接口
    :param name: str
    :return: 退出信息success or error
    """
    return "logout success"