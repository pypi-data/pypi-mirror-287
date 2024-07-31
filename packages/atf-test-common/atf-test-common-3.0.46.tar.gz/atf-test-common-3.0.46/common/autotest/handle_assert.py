from deepdiff import DeepDiff
from loguru import logger
import re
from common.autotest.handle_allure import allure_step
from common.data.data_process import DataProcess
from common.data.handle_common import req_expr, convert_json, extractor, is_not_bank, get_jpath, is_bank


def assert_result(res: dict, expect_str: str):
    """ 预期结果实际结果断言方法
    :param res: 实际响应结果
    :param expect_str: 预期响应内容，从excel中读取
    return None
    """
    # 后置sql变量转换
    expect_str = req_expr(expect_str, DataProcess.response_dict)
    expect_dict = convert_json(expect_str)
    index = 0
    for k, v in expect_dict.items():
        # 获取需要断言的实际结果部分
        actual = get_jpath(res, k)
        index += 1
        assert_equals(actual, v, f'返回结果【{k}】检查')


def assert_response(response, expect_str: str):
    """ 预期结果实际结果断言方法
    :param res: 实际响应结果
    :param expect_str: 预期响应内容，从excel中读取
    return None
    """
    # 后置sql变量转换
    expect_str = req_expr(expect_str, DataProcess.response_dict)
    try:
        expect_dict = convert_json(expect_str)
    except Exception:
        expect_dict = expect_str
    if isinstance(expect_dict,dict):
        index = 0
        for k, v in expect_dict.items():
            # 获取需要断言的实际结果部分
            if str(k).find('*ResCode') != -1:
                assert_equals(response.status_code, v, f'返回结果检查【状态码】')
            elif str(k).find('*ResBody') != -1:
                assert_equals(response.text, v, f'返回结果检查【返回内容】')
            else:
                try:
                    actual = get_jpath(response.json(), k)
                except:
                    actual = get_jpath(response.text, k)
                index += 1
                assert_equals(actual, v, f'返回结果检查【{k}】')

def assert_contain_response(response, expect_str: str):
    """ 预期结果实际结果断言方法
    :param res: 实际响应结果
    :param expect_str: 预期响应内容，从excel中读取
    return None
    """
    # 后置sql变量转换
    expect_str = req_expr(expect_str, DataProcess.response_dict)
    try:
        expect_dict = convert_json(expect_str)
    except Exception:
        expect_dict = expect_str
    if isinstance(expect_dict,dict):
        index = 0
        for k, v in expect_dict.items():
            # 获取需要断言的实际结果部分
            if str(k).find('*ResCode') != -1:
                assert_contains(response.status_code, v, f'返回结果【状态码】检查')
            elif str(k).find('*ResBody') != -1:
                assert_contains(response.text, v,f'返回结果【返回内容】检查')
            else:
                try:
                    actual = get_jpath(response.json(), k)
                except:
                    actual = get_jpath(response.text, k)
                index += 1
                assert_contains(actual, v, f'返回结果【{k}】检查')


def assert_excel_contain(res: dict, expect_str: str):
    """ 预期结果实际结果断言方法
    :param res: 实际响应结果
    :param expect_str: 预期响应内容，从excel中读取
    return None
    """
    # 后置sql变量转换
    expect_str = req_expr(expect_str, DataProcess.response_dict)
    expect_dict = convert_json(expect_str)
    index = 0
    for k, v in expect_dict.items():
        # 获取需要断言的实际结果部分
        actual = get_jpath(res, k)
        index += 1
        assert_contains(actual, v, f'返回结果【{k}】检查')


def assert_equals(actual, expect, desc:str='断言检查'):
    try:
        if isinstance(expect, dict):
            for k, v in expect.items():
                if isinstance(actual, dict):
                    assert_equal(expect[k],actual[k],desc)
                else:
                   assert_equal(expect[k],actual)
        elif isinstance(expect, list):
            for _index in range(len(expect)):
                if isinstance(actual, list):
                    assert_equal(expect[_index],actual[_index],desc)
                else:
                    assert_equal(expect[_index],actual,desc)
        elif isinstance(expect, str):
            if isinstance(actual, list):
                for _index in range(len(actual)):
                    assert_equal(actual[_index],expect, desc)
            else:
                assert_equal(actual, expect, desc)
        elif isinstance(expect, bool):
            if isinstance(actual,list):
                assert_equal(actual[0], expect, desc)
            else:
                assert_equal(actual, expect, desc)
        else:
            if isinstance(actual, list):
                assert_equal(actual[0], expect, desc)
            else:
                assert_equal(actual, expect, desc)
    except AssertionError:
        allure_step(f'{desc}【检查失败】', f'实际结果: {actual}  预期结果: {expect}')
        raise AssertionError(f'{desc} |- 实际结果: {actual}  预期结果: {expect}')

def assert_equal(actual, expect, desc :str='断言检查'):
    allure_step(f'{desc}', f'实际结果: {actual}  预期结果: {expect}')
    _actual = str(actual).strip()
    _expect = str(expect).strip()
    _type = _expect[0:4]
    if _type.find('<') != -1:
        _expect = _expect.replace('<', '', 1).strip()
        _actual, _expect = data_format(_actual, _expect)
        assert _actual < _expect
    elif _type.find('>') != -1:
        _expect = _expect.replace('>', '', 1).strip()
        _actual, _expect = data_format(_actual, _expect)
        assert _actual > _expect
    elif _type.find('==') != -1:
        _expect = _expect.replace('==', '', 1).strip()
        _actual, _expect = data_format(_actual, _expect)
        if _expect == '空':
            assert_bank(_actual)
        else:
            assert _actual == _expect
    elif _type.find('!=') != -1:
        _expect = _expect.replace('!=', '', 1).strip()
        _actual, _expect = data_format(_actual, _expect)
        if _expect == '空':
            assert_Nobank(_actual)
        else:
            assert _actual != _expect
    elif _type.find('IN=') != -1:
        _expect = _expect.replace('IN=', '', 1).strip()
        assert _expect in _actual
    else:
        assert _actual == _expect

def assert_equal_object(actual, expect, desc :str='断言检查'):
    allure_step(f'{desc}', f'实际结果: {actual}  预期结果: {expect}')
    _temp = DeepDiff(expect, actual)
    assert_equals('', _temp)



def data_format(_actual,_expect):
    _datatype = _expect[0:2]
    if _datatype.find('T')!=-1:
        _expect = _expect.replace('T', "").strip()
        _expect =DataProcess.getDateDiff(_expect)
        _actual =DataProcess.getDateDiff(_actual)
    return _actual,_expect


def assert_contains(actual, expect, desc: str = '断言检查'):
    allure_step(f'{desc}', f'实际结果:{actual} 包含 预期结果:{expect}')
    try:
        if isinstance(expect, dict):
            for k, v in expect.items():
                if isinstance(actual, dict):
                    assert str(expect[k]).strip() in str(actual[k]).strip()
                else:
                    assert str(expect[k]).strip() in str(actual).strip()
        elif isinstance(expect, list):
            for _index in range(len(expect)):
                if isinstance(actual, list):
                    assert str(expect[_index]).strip() in str(actual[_index]).strip()
                else:
                    assert str(expect[_index]).strip() in str(actual).strip()
        elif isinstance(expect, str):
            assert str(expect).strip() in str(actual).strip()
        else:
            assert expect in actual
    except AssertionError:
        raise AssertionError(f'{desc} |- 实际结果:{actual} 不包含 预期结果: {expect}')

def assert_Nobank(res, desc:str='断言检查'):
    allure_step(f'{desc}', f'预期结果:{res} 不为空')
    try:
        assert is_not_bank(res)
    except AssertionError:
        raise AssertionError(f'{desc} |- 实际结果:{res} 为空')

def assert_bank(res, desc:str='断言检查'):
    allure_step(f'{desc}', f'预期结果:{res} 为空')
    try:
        assert is_bank(res)
    except AssertionError:
        raise AssertionError(f'{desc} |- 实际结果:{res} 不为空')


def assert_not_contains(res, expect_str, desc:str = '断言检查'):
    allure_step(f'{desc}', f'实际结果:{res} 不包含 预期结果:{expect_str}')
    try:
        assert expect_str not in res
    except AssertionError:
        raise AssertionError(f'{desc} |- 实际结果:{res} 包含 预期结果: {expect_str}')

def assert_scene_result(res, expect_dict):
    global actual
    index = 0
    for k, v in expect_dict.items():
        # 获取需要断言的实际结果部分
        try:
            actual = extractor(res, k)
            index += 1
            logger.info(f'返回结果【{k}】检查,实际结果:{actual} | 预期结果:{v} | 断言结果 {actual == v}')
            allure_step(f'返回结果【{k}】检查,', f'实际结果:{actual} = 预期结果:{v}')
            assert actual == v
        except AssertionError:
            raise AssertionError(f'返回结果【{k}】检查失败, -|- 实际结果:{actual} || 预期结果: {v}')

# 比对数据
def compare_data(set_key, src_data, dst_data, noise_data, num):
    if isinstance(src_data, dict) and isinstance(dst_data, dict):
        """若为dict格式"""
        for key in dst_data:
            if key not in src_data:
                print("src不存在这个key")
                noise_data[key] = "src不存在这个key"
        for key in src_data:
            if key in dst_data:
                if src_data[key] != dst_data[key] and num == 1:
                    noise_data[key] = "容忍不等"
                if src_data[key] != dst_data[key] and num == 2:
                    noise_data[key] = {}
                    noise_data[key]["primary"] = src_data[key]
                    noise_data[key]["candidate"] = dst_data[key]
                """递归"""
                compare_data(key, src_data[key], dst_data[key], noise_data, num)
            else:
                noise_data[key] = ["dst不存在这个key"]
    elif isinstance(src_data, list) and isinstance(dst_data, list):
        """若为list格式"""
        if len(src_data) != len(dst_data) and len(set_key) != 0:
            print("list len: '{}' != '{}'".format(len(src_data), len(dst_data)))
            noise_data[set_key]["primary"] = str(src_data)
            noise_data[set_key]["candidate"] = str(dst_data)
            return
        if len(src_data) == len(dst_data) and len(src_data) > 1:
            for index in range(len(src_data)):
                for src_list, dst_list in zip(sorted(src_data[index]), sorted(dst_data[index])):
                    """递归"""
                    compare_data("", src_list, dst_list, noise_data, num)
        else:
            for src_list, dst_list in zip(sorted(src_data), sorted(dst_data)):
                """递归"""
                compare_data("", src_list, dst_list, noise_data, num)
    else:
        if str(src_data) != str(dst_data):
            print("src_data", src_data, "dst_data", dst_data)
    return noise_data

def equals(check_value, expect_value):
    assert check_value == expect_value, f'{check_value} == {expect_value})'


def less_than(check_value, expect_value):
    assert check_value < expect_value, f'{check_value} < {expect_value})'


def less_than_or_equals(check_value, expect_value):
    assert check_value <= expect_value, f'{check_value} <= {expect_value})'


def greater_than(check_value, expect_value):
    assert check_value > expect_value, f'{check_value} > {expect_value})'


def greater_than_or_equals(check_value, expect_value):
    assert check_value >= expect_value, f'{check_value} >= {expect_value})'


def not_equals(check_value, expect_value):
    assert check_value != expect_value, f'{check_value} != {expect_value})'


def string_equals(check_value, expect_value):
    assert str(check_value) == str(expect_value), f'{check_value} == {expect_value})'


def length_equals(check_value, expect_value):
    expect_len = _cast_to_int(expect_value)
    assert len(check_value) == expect_len, f'{len(check_value)} == {expect_value})'


def length_greater_than(check_value, expect_value):
    expect_len = _cast_to_int(expect_value)
    assert len(check_value) > expect_len, f'{len(check_value)} > {expect_value})'


def length_greater_than_or_equals(check_value, expect_value):
    expect_len = _cast_to_int(expect_value)
    assert len(check_value) >= expect_len, f'{len(check_value)} >= {expect_value})'


def length_less_than(check_value, expect_value):
    expect_len = _cast_to_int(expect_value)
    assert len(check_value) < expect_len, f'{len(check_value)} < {expect_value})'


def length_less_than_or_equals(check_value, expect_value):
    expect_len = _cast_to_int(expect_value)
    assert len(check_value) <= expect_len, f'{len(check_value)} <= {expect_value})'


def contains(check_value, expect_value):
    assert isinstance(check_value, (list, tuple, dict, str))
    assert expect_value in check_value, f'{len(expect_value)} in {check_value})'


def contained_by(check_value, expect_value):
    assert isinstance(expect_value, (list, tuple, dict, str))
    assert check_value in expect_value, f'{len(check_value)} in {expect_value})'


def regex_match(check_value, expect_value):
    assert isinstance(expect_value, str)
    assert isinstance(check_value, str)
    assert re.match(expect_value, check_value)


def startswith(check_value, expect_value):
    assert str(check_value).startswith(str(expect_value)), f'{str(check_value)} startswith {str(expect_value)})'


def endswith(check_value, expect_value):
    assert str(check_value).endswith(str(expect_value)), f'{str(check_value)} endswith {str(expect_value)})'


def _cast_to_int(expect_value):
    try:
        return int(expect_value)
    except Exception:
        raise AssertionError(f"%{expect_value} can't cast to int")






