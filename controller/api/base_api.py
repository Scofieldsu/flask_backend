# encoding: utf-8
from flask import json
from jsonrpc.backend.flask import api


@api.dispatcher.add_method
def test_api(param_dict, param_int, param_str, param_list):
    """
    :description  测试接口
    :param param_dict: dict:字典参数
    :param param_int: int:整型
    :param param_str: str:无默认值
    :param param_list: list:可以省略[]
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