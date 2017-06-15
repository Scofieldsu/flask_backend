# encoding: utf-8

def trans_str_to_dict(do_str):
    result = {}
    if not do_str:
        return result
    tem_list = do_str.split('\n')
    for x in tem_list:
        if ":description" in x:
            result["description"] = x.split(":description")[1]
        elif ":param" in x:
            params = x.split(":param")[1]
            if params.strip():
                tem = params.split(':')
                if len(tem) >= 2:
                    result[tem[0].strip()] = tem[1].strip()
        elif ":return:" in x:
            result["return"] = x.split(":return:")[1]
    return result


def dict_move_key(dict_a, dict_b, key):
    if key in dict_b:
        dict_a[key] = dict_b[key]
        dict_b.pop(key)
    return dict_a


def compose_api_info(key, api_dict):
    tem_res = {}
    tem_res["name"] = key
    doc_dict = trans_str_to_dict(api_dict[key].__doc__)
    tem_res = dict_move_key(tem_res, doc_dict, "description")
    tem_res = dict_move_key(tem_res, doc_dict, "return")
    tem_res["params"] = doc_dict
    return tem_res