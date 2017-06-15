- 安装依赖：pip install -r requirements.txt
- python run.py
 - - -
 - 运行后，localhost:5000/api_test/ 为api测试页面

 - 新增api在controller/apis.py 中添加，在其他文件中的api需要导入到controller/common中

 - 接口注释根据pycharm的自动补全，在参数后面填写数据类型即可；其中:description为接口描述（可选项）

 - 接口模型：

 ```python
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
    return result
 ```
