# Author: BL_30G
# Version: 0.5.0
import gc
from typing import Any, Union


# 1st function
def tidy_up_list(lst: list, bool_mode: bool = False, eval_mode: bool = False, float_mode: bool = False,
                 int_mode: bool = False, none_mode: bool = False) -> list:
    """
    A function to tidy up list(●ˇ∀ˇ●)

    :param float_mode:
    :param int_mode:
    :param none_mode:
    :param bool_mode: If you want to turn such as 'True' into True which it is in this list, you can turn on 'bool_mode' (～￣▽￣)～
    :param eval_mode: If you want to turn such as '[]' into [] which it is in this list, you can turn on 'eval_mode' (￣◡￣)
    :param lst:put list which you need to sorting and clean（￣︶￣）
    :return: the perfect list  ( ´◡` )

    """

    # 判断是否是list类型，否则返回形参原本值
    if type(lst) is not list and not (len(lst) <= 0):
        return lst

    bool_mode = bool(bool_mode)
    eval_mode = bool(eval_mode)
    float_mode = bool(float_mode)
    int_mode = bool(int_mode)

    _lst_types: list = []
    _point_j: int = 0
    _point_l: list = []
    _str_app_l: list = []
    _type_content: dict = {'str': [], 'int': [], 'float': [], 'lst': [], 'dic': [], 'set': [], 'tuple': [],
                           'complex': [],
                           'None': []}

    # 保存原有特殊变量原本值
    for i in range(len(lst)):
        if isinstance(lst[i], str) and (lst[i] not in _type_content['str']):
            _type_content['str'].append(lst[i])

        if isinstance(lst[i], int) and (lst[i] not in _type_content['int']):
            _type_content['int'].append(lst[i])

        if isinstance(lst[i], float) and (lst[i] not in _type_content['float']):
            _type_content['float'].append(lst[i])

        if type(lst[i]) is None and (lst[i] not in _type_content['None']):
            _type_content['None'].append(lst[i])

        if type(lst[i]) is list and (lst[i] not in _type_content['lst']):
            _type_content['lst'].append(lst[i])

        if type(lst[i]) is dict and (lst[i] not in _type_content['dic']):
            _type_content['dic'].append(lst[i])

        if type(lst[i]) is set and (lst[i] not in _type_content['set']):
            _type_content['set'].append(lst[i])

        if type(lst[i]) is tuple and (lst[i] not in _type_content['tuple']):
            _type_content['tuple'].append(lst[i])
        if type(lst[i]) is complex and (lst[i] not in _type_content['complex']):
            _type_content['complex'].append(lst[i])

        lst[i] = str(lst[i])

    # 排序+去除重复值
    lst = list(set(lst))
    for i in range(len(lst)):
        lst[i] = str(lst[i])
    lst = sorted(lst, key=str.lower)

    # 判断列表值是何类型1
    for i in range(len(lst)):
        _point_l.append([])
        _str_app_l.append([])
        for j in lst[i]:
            if 48 <= ord(j) <= 57:
                continue
            elif j == '.':
                if not _point_l[i]:
                    _point_l[i].append(True)
                else:
                    continue
            else:
                if not _str_app_l[i]:
                    _str_app_l[i].append(True)
                else:
                    continue

    # 判断列表值是何类型2
    for i in range(len(_point_l)):
        if True in _str_app_l[i]:
            _lst_types.append('str')
        elif True in _point_l[i] and _str_app_l[i] == []:
            for j in range(len(lst[i])):
                if lst[i][j] == '.':
                    _point_j += 1
            if _point_j == 1:
                _lst_types.append('float')
                _point_j = 0
            else:
                _lst_types.append('str')
                _point_j = 0
        else:
            _lst_types.append('int')

    # 转换类型
    for i in range(len(_lst_types)):
        if _lst_types[i] == 'str':
            if eval_mode:
                try:
                    lst[i] = eval(lst[i])
                except:
                    pass
            pass
        try:
            if _lst_types[i] == 'float':
                lst[i] = float(lst[i])
            if _lst_types[i] == 'int':
                lst[i] = int(lst[i])
        except ValueError:
            pass

    # code burger(bushi     (将收集到的特殊数据插入回列表)
    for i in range(len(_type_content['complex'])):
        lst.remove(str(_type_content['complex'][i]))
        lst.append(_type_content['complex'][i])
    for i in range(len(_type_content['tuple'])):
        lst.remove(str(_type_content['tuple'][i]))
        lst.append(_type_content['tuple'][i])
    for i in range(len(_type_content['lst'])):
        lst.remove(str(_type_content['lst'][i]))
        lst.append(_type_content['lst'][i])
    for i in range(len(_type_content['set'])):
        lst.remove(str(_type_content['set'][i]))
        lst.append(_type_content['set'][i])
    for i in range(len(_type_content['dic'])):
        lst.remove(str(_type_content['dic'][i]))
        lst.append(_type_content['dic'][i])

    if bool_mode:
        for i in range(len(lst)):
            if lst[i] == 'True':
                lst[i] = bool(1)
            elif lst[i] == 'False':
                lst[i] = bool(0)

    del _lst_types, _point_j, _point_l, _str_app_l, _type_content
    gc.collect()

    return lst


# 2nd function
def deeply_tidy_up_list(lst: list) -> list:
    """
    This Function can search list elements and tidy up it too(‾◡‾)

    :param lst:put list which you need to sorting and clean（￣︶￣）
    :return: the perfect list  ( ´◡` )
    """

    if type(lst) is not list:
        return lst

    _j: int = 0
    lst = tidy_up_list(lst)

    for _i in lst:
        if type(_i) is list:
            lst[_j] = deeply_tidy_up_list(_i)
        _j += 1
    return lst


# 3rd function
def bubble_sort(lst: list, if_round: bool = False, in_reverse_order: bool = False) -> list:
    """
    A simple bubble sort function ~(￣▽￣)~*\n

    :param lst: The list you need to sort
    :param if_round: Rounding floating-point numbers
    :param in_reverse_order: Reverse the list
    :return: The sorted list
    """

    if type(lst) is not list:
        return lst

    _i: int = 0
    if_round = bool(if_round)
    lst_T = lst.copy()

    for _i in range(len(lst_T)):
        if (not (isinstance(lst_T[_i], int) or isinstance(lst_T[_i], float))) or len(lst_T) == 0:
            return lst_T

    if if_round:
        from math import ceil
        for _i in range(len(lst_T)):
            if isinstance(lst_T[_i], float):
                lst_T[_i] = ceil(lst_T[_i])

    lst_len = len(lst_T)
    for _i in range(lst_len):
        for _j in range(lst_len - 1 - _i):
            if in_reverse_order:
                if lst_T[_j + 1] >= lst_T[_j]:
                    lst_T[_j], lst_T[_j + 1] = lst_T[_j + 1], lst_T[_j]
            else:
                if lst_T[_j + 1] <= lst_T[_j]:
                    lst_T[_j], lst_T[_j + 1] = lst_T[_j + 1], lst_T[_j]

    try:
        del _i, _j
    except UnboundLocalError:
        pass
    gc.collect()

    return lst_T


# 4th function
# Big Project(Finished!)
def list_calculation(*args: list, calculation: str = "+", multi_calculation: str = "", nesting: bool = False) -> list:
    """
    The function for perform calculation on multiple lists
    :param args: The lists to calculation
    :param calculation: An calculation symbol used between all lists (Only one)(default:"+")(such as "+", "-", "*", "/", "//", "%")
    :param multi_calculation: Different calculation symbols between many lists (Use ',' for intervals)
    :param nesting: If the lists you want to calculation are in a list, You should turn on 'nesting' to clean the nesting list
    :return: The result of lists
    """

    if len(args) <= 0 or len(calculation) <= 0:
        raise ValueError("No any list given")

    if len(calculation) > 1:
        raise ValueError("the length of calculation symbol can only be 1")

    if nesting:
        args = eval(str(args)[1:len(str(args)) - 2:])

    args = list(args)
    if_multi_calculation: bool = False
    if len(multi_calculation) != 0:
        if_multi_calculation = True
        multi_calculation = multi_calculation[:len(args) - 1:]
    length: dict = {}
    length_keys: list = []
    length_values: list = []

    # 清除掉长度为0的list元素和不是list类的元素
    for _i in range(len(args)):
        if not (isinstance(args[_i], list) or len(args[_i]) == 0):
            args.pop(_i)

    # 如果list里面的list的元素不是int或者float就报错
    for _i in range(len(args)):
        for _j in range(len(args[_i])):
            if not (isinstance(args[_i][_j], int) or isinstance(args[_i][_j], float)):
                raise ValueError(f"element cannot be {type(args[_i][_j])}")

    # 记录每个列表的长度
    # _i是第几个列表
    for _i in range(len(args)):
        length.update({_i: len(args[_i])})

    # 依照长度从小到大排序
    length_l = sorted(length.items(), key=lambda x: x[1])

    # key对应的是列表里面的第几个列表,value对应的是列表内的列表长度
    for key, value in length_l:
        length_keys.append(key)
        length_values.append(value)

    # 将列表倒序变成从大到小排序
    length_keys, length_values = list(reversed(length_keys)), list(reversed(length_values))
    # result取长度最长的列表
    result = args[length_keys[0]].copy()

    if not if_multi_calculation:
        for _i in range(len(length_l)):
            try:
                for _j in range(length_values[_i + 1]):
                    if calculation == "+":
                        result[_j] += (args[length_keys[_i + 1]].copy())[_j]
                    elif calculation == "-":
                        result[_j] -= (args[length_keys[_i + 1]].copy())[_j]
                    elif calculation == "*":
                        result[_j] *= (args[length_keys[_i + 1]].copy())[_j]
                    elif calculation == "**":
                        result[_j] **= (args[length_keys[_i + 1]].copy())[_j]
                    elif calculation == "/":
                        result[_j] /= (args[length_keys[_i + 1]].copy())[_j]
                    elif calculation == "//":
                        result[_j] //= (args[length_keys[_i + 1]].copy())[_j]
                    elif calculation == "%":
                        result[_j] %= (args[length_keys[_i + 1]].copy())[_j]
            except IndexError:
                pass

    if if_multi_calculation:
        calculation_lst = multi_calculation.split(",")
        for _i in range(len(length_l)):
            try:
                for _j in range(length_values[_i + 1]):
                    if calculation_lst[_i] == "+":
                        result[_j] += (args[length_keys[_i + 1]].copy())[_j]
                    elif calculation_lst[_i] == "-":
                        result[_j] -= (args[length_keys[_i + 1]].copy())[_j]
                    elif calculation_lst[_i] == "*":
                        result[_j] *= (args[length_keys[_i + 1]].copy())[_j]
                    elif calculation_lst[_i] == "**":
                        result[_j] **= (args[length_keys[_i + 1]].copy())[_j]
                    elif calculation_lst[_i] == "/":
                        result[_j] /= (args[length_keys[_i + 1]].copy())[_j]
                    elif calculation_lst[_i] == "//":
                        result[_j] //= (args[length_keys[_i + 1]].copy())[_j]
            except IndexError:
                pass

    try:
        del _i, _j, length, length_l, length_keys, length_values
    except UnboundLocalError:
        pass
    gc.collect()

    return result


# 5th function
def var_in_list(lst: list, __class: type, return_lst: bool = False, only_return_lst: bool = False) -> Union[int, tuple, list]:
    """
    Returns the number of variables in the list that match the type given by the user
    :param lst: The list
    :param __class: The class of variable you want to find
    :param return_lst: Returns a list of variables that match the type
    :param only_return_lst: Only returns a list of variables that match the type
    :return:
    """
    if return_lst and only_return_lst:
        raise ValueError("return_lst and only_return_lst cannot be True at the same time")

    def in_def_var_in_list(lst2: list) -> Union[int, tuple, list]:
        if return_lst:
            if globals().get("$all_result") is None:
                globals().update({"$all_result": 0})
            if globals().get("$all_result_lst") is None:
                globals().update({"$all_result_lst": list([])})
        elif only_return_lst:
            if globals().get("$all_result_lst") is None:
                globals().update({"$all_result_lst": list([])})
        else:
            if globals().get("$all_result") is None:
                globals().update({"$all_result": 0})
        for _i in range(len(lst2)):
            if isinstance(lst2[_i], __class):
                if return_lst:
                    globals().update({"$all_result": globals().get("$all_result") + 1}), globals().get("$all_result_lst").append(lst2[_i])
                elif only_return_lst:
                    globals().get("$all_result_lst").append(lst2[_i])
                else:
                    globals().update({"$all_result": globals().get("$all_result") + 1})
            elif isinstance(lst2[_i], list):
                in_def_var_in_list(lst2[_i])
        if return_lst:
            return globals().get("$all_result"), globals().get("$all_result_lst")
        elif only_return_lst:
            return globals().get("$all_result_lst")
        else:
            return globals().get("$all_result")

    return_lst = bool(return_lst)
    result = in_def_var_in_list(lst)
    if return_lst:
        globals().pop("$all_result"), globals().pop("$all_result_lst")
    elif only_return_lst:
        globals().pop("$all_result_lst")
    else:
        globals().pop("$all_result")
    return result


# 6th function
def in_list_calculation(lst: list, calculation: str = "+", multi_calculation: str = "") -> Union[int, float, list]:
    """
    A function to calculation all the int or float in the list
    :param lst: The list
    :param calculation: An calculation symbol used between all lists (Only one)(default:"+")(such as "+", "-", "*", "/", "//", "%")
    :param multi_calculation: Different calculation symbols between many lists (Use ',' for intervals)
    :return:
    """
    import gc

    if not isinstance(lst, list):
        return lst

    nums_lst = var_in_list(lst, int, only_return_lst=True) + var_in_list(lst, float, only_return_lst=True)

    if not nums_lst:
        return lst
    else:
        result: int = nums_lst[0]
        if multi_calculation == "":
            result: int = nums_lst[0]
            nums_lst.pop(0)
            for _i in range(len(nums_lst)):
                if calculation == "+":
                    result += nums_lst[_i]
                elif calculation == "-":
                    result -= nums_lst[_i]
                elif calculation == "*":
                    result *= nums_lst[_i]
                elif calculation == "**":
                    result **= nums_lst[_i]
                elif calculation == "/":
                    result /= nums_lst[_i]
                elif calculation == "//":
                    result //= nums_lst[_i]
                elif calculation == "%":
                    result %= nums_lst[_i]
        else:
            lst_cal = multi_calculation.split(",")
            if len(lst_cal) > len(nums_lst)-1:
                lst_cal = list(multi_calculation)[:len(nums_lst):]
            elif len(lst_cal) < len(nums_lst)-1:
                lst_cal_copy = lst_cal.copy()
                lst_cal_copy_subscript: int = 0
                tmp_lst = [_ for _ in range(0, len(nums_lst), len(lst_cal))]
                for _i in range(len(nums_lst)-1 - len(lst_cal)):
                    if _i in tmp_lst:
                        lst_cal_copy_subscript = 0
                    lst_cal.append(lst_cal_copy[lst_cal_copy_subscript])
                    lst_cal_copy_subscript += 1
            for _i in range(len(nums_lst)):
                if _i == 0:
                    continue
                if _i == len(lst_cal)+1:
                    break
                if lst_cal[_i-1] == "+":
                    result += nums_lst[_i]
                elif lst_cal[_i-1] == "-":
                    result -= nums_lst[_i]
                elif lst_cal[_i-1] == "*":
                    result *= nums_lst[_i]
                elif lst_cal[_i - 1] == "**":
                    result **= nums_lst[_i]
                elif lst_cal[_i-1] == "/":
                    result /= nums_lst[_i]
                elif lst_cal[_i-1] == "//":
                    result //= nums_lst[_i]
                elif lst_cal[_i-1] == "%":
                    result %= nums_lst[_i]

    try:
        del nums_lst
        del lst_cal
        del lst_cal_copy, lst_cal_copy_subscript, tmp_lst
    except UnboundLocalError:
        pass
    gc.collect()

    return result


# 7th function
def get_variable(value: Any) -> list:
    """
    A function to get the name of variable
    :param value: the value of variable
    :return: the name of variable
    """

    eligible_lst = []

    for __temp, __temp2 in globals().items():
        if __temp2 == value:
            eligible_lst.append(__temp)
    return eligible_lst


# 8th function
def index_len(__obj) -> int:
    """
    Return the number of items in a container(= len(__obj)-1)
    :param __obj
    :return
    """

    i: int = -1
    if isinstance(__obj, list) or isinstance(__obj, dict) or isinstance(__obj, set):
        __obj = iter(__obj.copy())
    while True:
        try:
            next(__obj)
            i += 1
        except StopIteration:
            return i


# str functions area
# 9th function
def replace_str(string: str, __c: str, __nc: str, num=0) -> str:
    # This Function is Finished!~ (*^▽^*)
    """
    Change the character in the string to a new character, but unlike "str.replace()", num specifies the number of original strs that that need to change (not the maximum times of changes)
    :param string: The string
    :param __c: Original character
    :param __nc: New character
    :param num: How many character(default is Zero(replace all Eligible character))
    :return:
    """

    if (len(str(__c)) == 0) or (len(str(string)) == 0):
        raise ValueError("Original character cannot be empty!")

    if len(__c) == 1 and __c not in list(str(string)):
        return string

    string = str(string)
    __c = str(__c)
    __nc = str(__nc)
    lst_string = list(string)

    if len(__c) == 1 and num == 0:
        return string.replace(__c, __nc)

    elif len(__c) == 1 and num != 0:
        times: int = 0
        _i: int = 0
        for _i in range(len(lst_string)):
            if lst_string[_i] == __c:
                times += 1
                if times == num:
                    break
        if times != num:
            return string
        lst_string[_i] = __nc
        new_string = str("".join(lst_string))
        del _i, times, lst_string
        gc.collect()
        return new_string

    elif len(__c) > 1 and num == 0:
        return string.replace(__c, __nc)

    elif len(__c) > 1 and num != 0:
        temp_bool: bool = False
        times: int = 0
        _i: int = 0
        while not (_i == len(lst_string) - len(__c) or times >= num):
            temp = lst_string[_i:len(__c) + _i:]
            temp = str("".join(temp))
            if temp == __c:
                _i += len(__c)
                times += 1
                continue
            _i += 1
        if times != num:
            return string
        temp2 = list(__nc)
        _i -= 1
        for _j in range(len(__nc)):
            if len(__nc) > len(__c):
                if _j >= len(__c):
                    lst_string.insert(int(_i + _j), temp2[_j])
                else:
                    lst_string[_i + _j] = temp2[_j]
            else:
                temp_bool = True
                break
        if temp_bool and len(__nc) != 0:
            for _j in range(len(__c) - len(__nc)):
                lst_string.pop(_i)
            for _j in range(len(__nc)):
                lst_string[_i + _j] = temp2[_j]
        elif len(__nc) == 0:
            for _j in range(len(__c)):
                lst_string.pop(_i)
        new_string = str("".join(lst_string))
        try:
            del _i, _j, temp, temp2, temp_bool, times
        except UnboundLocalError:
            pass
        gc.collect()
        return new_string


# 10th function
def reverse_str(string: str) -> str:
    """
    A very, very easy function to reverse str（混水分
    :param string: The string you want to reverse
    :return: the reversed str
    """
    if len(str(string)) <= 0:
        return string
    return str("".join(list(reversed(list(str(string))))))


# 11th function
def statistics_str(string: str) -> tuple:
    """
    Return the statistics of the string,
    include the sort of the character according to ASCII Table and the appeared numbers of the character in this string
    :param string: The string you need statistics
    :return: The statistics of the string
    """

    from collections import Counter

    string = str(string)
    lst_string = list(string).copy()
    all_l: list = []
    all_d: dict = {}

    # Ascii部分
    for _i in lst_string:
        all_l.append(ord(_i))

    all_l = bubble_sort(all_l)

    for _i in range(len(all_l)):
        all_d.update({f"{chr(all_l[_i])}": all_l[_i]})

    # 次数部分
    num = str(Counter(lst_string))[8::]
    num = eval(num[:len(num) - 1:])

    return all_d, num


# 12th function
def find_list(lst: list, __fc: str, start: bool = False, mid: bool = False, end: bool = False) -> list:
    """
    Based on the string given by the user, find the string that contains this string in the list.
    :param lst: The list you want to find
    :param __fc: The character in list in string
    :param start: Only find on list start
    :param mid: Only find on list middle
    :param end: Only find on list end
    :return: List of find result
    """

    if not (isinstance(lst, list)):
        return lst

    find: list = []
    _i: int = 0
    __fc, start, mid, end = str(__fc), bool(start), bool(mid), bool(end)

    for _i in range(len(lst)):
        if __fc in lst[_i] and start and not (mid and end) and _i == 0:
            find.append(lst[_i])
        elif __fc in lst[_i] and mid and not (start and end) and _i == len(lst) // 2:
            find.append(lst[_i])
        elif __fc in lst[_i] and end and not (start and mid) and _i == len(lst) - 1:
            find.append(lst[_i])
        else:
            if start and mid:
                if (__fc in lst[_i] and _i == 0) or (__fc in lst[_i] and _i == len(lst) // 2):
                    find.append(lst[_i])
            elif start and end:
                if (__fc in lst[_i] and _i == 0) or (__fc in lst[_i] and _i == len(lst) - 1):
                    find.append(lst[_i])
            elif mid and end:
                if (__fc in lst[_i] and len(lst) // 2) or (__fc in lst[_i] and _i == len(lst) - 1):
                    find.append(lst[_i])
            else:
                if __fc in lst[_i]:
                    find.append(lst[_i])

    try:
        del _i
    except UnboundLocalError:
        pass
    gc.collect()

    return find


# bool area
# 13th function
def can_variable(string: str) -> bool:
    """
    The function can judge the string can or cannot be variable
    :param string:
    :return:
    """

    string = str(string)
    judgment_lst = ["False", "None", "True", "and", "as", "assert", "break", "case", "class", "continue", "def", "del", "elif",
                    "else", "except", "finally", "for", "from", "global", "if", "import", "in", "is", "lambda",
                    "match", "nonlocal", "not", "or",
                    "pass", "raise", "return", "try", "while", "with", "yield"]
    C_variable: bool = True

    if string in judgment_lst:
        C_variable = False
    elif not string.isalpha():
        C_variable = False
    elif 48 <= ord(string[0:]) <= 57:
        C_variable = False

    del judgment_lst
    gc.collect()
    return C_variable
