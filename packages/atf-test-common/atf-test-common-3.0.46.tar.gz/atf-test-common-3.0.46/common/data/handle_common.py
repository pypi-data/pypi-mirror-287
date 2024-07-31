import os
import re
import json
from jsonpath import jsonpath
from loguru import logger
from common.common.constant import Constant
from common.plugin.hooks_plugin import exec_func



def extractor(obj: dict, expr: str = '.', error_flag: bool = False) -> object:
    """
    根据表达式提取字典中的value，表达式, . 提取字典所有内容， $.case 提取一级字典case， $.case.data 提取case字典下的data
    :param obj :json/dict类型数据
    :param expr: 表达式, . 提取字典所有内容， $.case 提取一级字典case， $.case.data 提取case字典下的data
    $.0.1 提取字典中的第一个列表中的第二个的值
    """
    try:
        if isinstance(obj, str):
            obj = json.loads(obj)
        result = jsonpath(obj, expr)[0]
    except Exception as e:
        if error_flag:
            logger.warning(f'{expr} - 提取不到内容！{e}')
        result = expr
    return result

def get_jpath(obj: dict, expr: str = '.', error_flag: bool = False) -> object:
    """
    根据表达式提取字典中的value，表达式, . 提取字典所有内容， $.case 提取一级字典case， $.case.data 提取case字典下的data
    :param obj :json/dict类型数据
    :param expr: 表达式, . 提取字典所有内容， $.case 提取一级字典case， $.case.data 提取case字典下的data
    $.0.1 提取字典中的第一个列表中的第二个的值
    """
    try:
        result = jsonpath(obj, expr)
    except Exception as e:
        if error_flag:
            logger.warning(f'{expr} - 提取不到内容！{e}')
        result = expr
    return result

def req_expr(content: str, data: dict = None, expr: str = '\\${(.*?)}', _no_content: int = 0, _dataType:bool=False,_replace:int=0) -> str:
    """从请求参数的字符串中，使用正则的方法找出合适的字符串内容并进行替换
    :param content: 原始的字符串内容
    :param data: 在该项目中一般为响应字典，从字典取值出来
    :param expr: 查找用的正则表达式
    return content： 替换表达式后的字符串
    """
    if _replace == 0:
        if isinstance(content, str):
            content = content.replace('\\', '')
        else:
            content = str(content).replace('\\', '')
    else:
        content = str(content)
    for i in re.findall(expr, content):
        if i.find(".") >= 0:
            from common.plugin.data_bus import DataBus
            _content = DataBus.get_key(i)
        elif i.find("|") >= 0:
            _arr = i.split('|')
            if get_system_key(f'{_arr[0]}') is None:
                _content = str(extractor(data, _arr[0]))
                if _content == _arr[0]:
                    _content = i
            else:
                from common.plugin.data_bus import DataBus
                _content = DataBus.get_key(_arr[0])
        elif get_system_key(f'{i}') is None:
            _content = str(extractor(data, i))
        else:
            _content = get_system_key(f'{i}',_dataType)

        if _content is None or _content == f'{i}':
            if i.find("|") >= 0:
                _arr = i.split('|')
                content = content.replace('${' + f'{i}' + '}', _arr[1])
            elif i.find(".json") >= 0 or i.find(".txt") >= 0 or i.find(".yaml") >= 0 or i.find(".xml") >= 0:
                from common.plugin.file_plugin import FilePlugin
                fileData = FilePlugin.load_data(i)
                content = content.replace('${' + f'{i}' + '}', str(fileData))
            else:
                if _no_content == 0:
                    content = content.replace('${' + f'{i}' + '}', Constant.DATA_NO_CONTENT)
                if _no_content == 1:
                    content = content.replace('${' + f'{i}' + '}', f'{i}')
                if _no_content == 2:
                    content = content.replace('${' + f'{i}' + '}', '')
                if _no_content == 4:
                    content = content.replace(f'{i}', f'{i}')
                if _no_content == 5:
                    content1 = {key: val for key, val in convert_json(content).items() if (val != ('${' + f'{i}' + '}'))}
                    content = str(content1)
                if _no_content == 6:
                    content = content.replace('${' + f'{i}' + '}', '0.000000000')
        else:
            content = content.replace('${' + f'{i}' + '}', _content)

        # 增加自定义函数得的调用，函数写在tools/hooks.py中
        for func in re.findall('@(.*?)@', content):
            try:
                content = content.replace(f'@{func}@', exec_func(func))
            except Exception as e:
                logger.error(e)
                continue
    return content



# 替换表格数据
def replace_data(data, cls):
    """
    替换数据
    :param data: 要进行替换的用例数据(字符串)
    :param cls:  测试类
    :return:
    使用方法：
    读取表格中data数据，调用此方法传入data数据和类名进行替换，再时使用eval转为json类型
    item['data'] = replace_data(item['data'], AddTestCase)
    params = eval(item['data'])
    """
    while re.search('#(.+?)#', data):
        res = re.search('#(.+?)#', data)
        item = res.group()
        attr = res.group(1)
        value = getattr(cls, attr)
        # 进行替换
        data = data.replace(item, str(value))
    return data


def convert_json(dict_str: str) -> dict:
    """
    :param dict_str: 长得像字典的字符串
    return json格式的内容
    """
    if isinstance(dict_str,str):
        try:
            if 'None' in dict_str:
                dict_str = dict_str.replace('None', 'null')
            if 'True' in dict_str:
                dict_str = dict_str.replace('True', 'true')
            if 'False' in dict_str:
                dict_str = dict_str.replace('False', 'false')
            dict_str = json.loads(dict_str)
        except Exception as e:
            if 'null' in dict_str:
                dict_str = dict_str.replace('null', 'None')
            if 'true' in dict_str:
                dict_str = dict_str.replace('true', 'True')
            if 'false' in dict_str:
                dict_str = dict_str.replace('false', 'False')
            dict_str = eval(dict_str)
    return dict_str

def get_system_key(str_key, _type=False):
    """
    从环境变量中获取值
    :param str_key:
    :return:
    """
    temp = None
    if os.getenv(str_key.strip()) is not None:
        temp = str(os.getenv(str_key.strip()))
    else:
        if os.getenv(str_key.lower().strip()) is not None:
            temp = str(os.getenv(str_key.lower().strip()))
    if os.getenv((str_key + Constant.DATA_TYPE).lower().strip()) is not None and _type:
        if os.getenv((str_key + Constant.DATA_TYPE).lower().strip()) == Constant.DATA_DIC:
            temp = eval(temp)
        if os.getenv((str_key + Constant.DATA_TYPE).lower().strip()) == Constant.DATA_LIST:
            temp = list(temp)
    return temp


def set_system_key(str_key,str_value,_replace:bool=False):
    """
    把值设置到环境变量中
    :param str_key:
    :param str_value:
    :param _replace: 如果存在，是否替换原来的Key
    :return:
    """
    try:
        if _replace:
            if str_value is not None and isinstance(str_value, str):
                os.environ[str_key.lower().strip()] = str_value.strip()
            elif str_value is not None and isinstance(str_value, dict):
                os.environ[str_key.lower().strip()] = str(str_value)
                os.environ[(str_key + Constant.DATA_TYPE).lower().strip()] = Constant.DATA_DIC
            elif str_value is not None and isinstance(str_value, list):
                os.environ[str_key.lower().strip()] = str(str_value)
                os.environ[(str_key + Constant.DATA_TYPE).lower().strip()] = Constant.DATA_LIST
            elif str_value is not None:
                os.environ[str_key.lower().strip()] = str(str_value)
        else:
            _old = get_system_key(str_key)
            if _old is None:
                if str_value is not None and isinstance(str_value, str):
                    os.environ[str_key.lower().strip()] = str_value.strip()
                elif str_value is not None and isinstance(str_value, dict):
                    os.environ[str_key.lower().strip()] = str(str_value)
                    os.environ[(str_key + Constant.DATA_TYPE).lower().strip()] = Constant.DATA_DIC
                elif str_value is not None and isinstance(str_value, list):
                    os.environ[str_key.lower().strip()] = str(str_value)
                    os.environ[(str_key + Constant.DATA_TYPE).lower().strip()] = Constant.DATA_LIST
                elif str_value is not None:
                    os.environ[str_key.lower().strip()] = str(str_value)
    except Exception as e:
        logger.warning(f'保存DataBus中数据异常KEY:{str_key} Value:{str_value} 异常信息:' + repr(e))



def print_databus_info(_key,_desc):
    _value = get_system_key(_key)
    if _value is not None:
        logger.info(f'{_desc}:{_value}')
    else:
        logger.info(f'{_desc}:')

def print_info(info):
    if is_not_bank(get_system_key('logType')) and get_system_key('logType').strip().lower() == 'info':
            logger.info(info)


def print_debug(info):
    if is_not_bank(get_system_key('logType')) and get_system_key('logType').strip().lower() == 'debug':
            logger.info(info)




def is_bank(_str):
    if isinstance(_str, str):
        if _str is None:
            return True
        if _str.strip() == '':
            return True
    else:
        if not _str:
            return True
    return False

def is_not_bank(data):
    try:
        if isinstance(data, bool):
            return data
        if data is None:
            return False
        if isinstance(data, str):
            _data = data
        else:
            _data = str(data)
        if _data.strip() == '':
            return False
        else:
            return True
    except Exception as e:
        logger.info('判断数据是否为空异常,数据：' + data)
        return True

def format_caseName(_str:str):
    return _str.replace("&amp;", "&").replace("&ldquo;", "“").replace("&rdquo;", "”") \
        .replace("&mdash;", "") \
        .replace("&quot;", "\"").replace("&gt;", ">") \
        .replace("&lt;", "<").replace("", "").strip()

def singleton(cls):
    # 创建一个字典用来保存类的实例对象
    _instance = {}

    def _singleton(*args, **kwargs):
        # 先判断这个类有没有对象
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)  # 创建一个对象,并保存到字典当中
        # 将实例对象返回
        return _instance[cls]

    return _singleton

def convert_json_dict(_json):
    _new = {}
    for key in _json.keys():
        if isinstance(_json.get(key), str):
            if str(_json.get(key)).find(Constant.DATA_NO_CONTENT) < 0:
                _new[key] = _json.get(key)
        else:
            if isinstance(_json.get(key), dict):
                _new[key] = convert_json_dict(_json.get(key))
            else:
                _new[key] = _json.get(key)
    return _new

def convert_json_bank(content, data):
    _str = req_expr(content=content, data=data, _no_content=0)
    _str = _str.replace(Constant.DATA_NO_CONTENT + ",", '"' + Constant.DATA_NO_CONTENT + '",')
    from common.data.data_process import DataProcess
    _json = DataProcess.handle_data(_str)
    if _json is None:
        return None
    else:
        return json.dumps(convert_json_dict(_json), ensure_ascii=False)

def objecttodict(obj):
    """
     复杂对象转成dict的方法
    """
    dict_o = obj.__dict__
    for key, value in dict_o.items():
        print(key, type(value))
        if isinstance(value, (str, int)):  # 不处理str,int的情况
            pass
        elif value is None:
            pass
        elif isinstance(value, list):  # 处理list的情况
            valuelist = []
            for l in value:
                if isinstance(l, (str, int)):
                    valuelist.append(l)
                else:
                    valuelist.append(objecttodict(l))
            dict_o[key] = valuelist
        elif isinstance(value, dict):
            pass  # 不处理dict的情况
        else:  # 处理普通对象
            dict_o[key] = objecttodict(value)
    return dict_o



if __name__ == '__main__':
    from common.data.data_process import DataProcess
    print(objecttodict(DataProcess))






