# encoding: utf-8
from flask import json
from jsonrpc.backend.flask import api


@api.dispatcher.add_method
def my_method2(param_dict, param_int, param_str, param_list):
    """
    :description  测试接口2
    :param param_dict: dict
    :param param_int: int
    :param param_str: str
    :param param_list: list
    :return: code or message
    """

    data1 = json.loads(param_dict)
    data2 = param_int
    data3 = param_str
    data4 = param_list
    result = {
        "param_dict": data1,
        "param_int": data2,
        "param_str": data3,
        "param_list": data4
    }
    return result