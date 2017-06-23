# encoding: utf-8
from flask import json
from jsonrpc.backend.flask import api


api_add = api.dispatcher.add_method


@api_add
def test_api(my_dict, my_int, my_str, my_list, my_datetime):
    """
    :description  测试接口
    :param my_dict: dict:字典参数
    :param my_int: int:整型
    :param my_str: str:无默认值
    :param my_list: list:可以省略[]
    :param my_datetime: datetime :时间戳
    :return: code or message
    """

    data1 = json.loads(my_dict)
    data2 = my_int
    data3 = my_str
    data4 = my_list
    data5 = my_datetime
    result = {
        "loads之前的my_dict": my_dict,
        "my_dict": data1,
        "my_int": data2,
        "my_str": data3,
        "my_list": data4,
        "my_datetime": data5
    }
    return result