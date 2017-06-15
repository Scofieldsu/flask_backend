# encoding: utf-8

from utils.api_tools import compose_api_info
from apis import *


@api.dispatcher.add_method
def my_method(param_dict, param_int, param_str, param_list):
    """
    :description  测试接口
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


@api.dispatcher.add_method
def get_all_api(*args, **kwargs):
    """
    :description 获取接口信息
    :param args:str
    :param kwargs:str
    :return: 所有接口信息
    """
    api_dict = api.dispatcher.method_map
    api_name_list = api_dict.keys()
    result = {}
    for i in api_name_list:
        item = {}
        item = compose_api_info(i, api_dict)
        result[i] = item
    result.pop("get_all_api")
    return result



def get_all_api_temp(*args, **kwargs):
    result = {'login': {'name': 'login', 'description': '登录接口', 'return': '返回信息', 'params': {'login_name': 'str', "password": "str"}},
              'logout': {'name': 'logout', 'description': '退出', 'return': '返回信息',  'params': {"name": "str", "pwd": "str"}}}
    return result