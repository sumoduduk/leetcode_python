from typing import List


def pop_middle(x: List[int]) -> List[int]:
    xLen = len(x)
    if xLen % 2 != 0:
        x.pop(xLen // 2)

    new_len = len(x)
    # print(f"new len is {new_len}")
    return x


def transform_list(x: List[int]) -> List[int]:
    # print(f" list old is {x}")

    for i in range(len(x)):
        last = x.pop()
        x.insert(i, last)

    # print(f" list new is {x}")
    return x


def test_transform_list_1():
    list_input = [1, 4, 5, 6]
    list_target = [6, 5, 4, 1]
    assert transform_list(list_input) == list_target


def test_transform_list_2():
    list_input = [1, 4]
    list_target = [4, 1]
    assert transform_list(list_input) == list_target


def test_transform_list_3():
    list_input = [1, 4, 3, 5, 6]
    list_target = [6, 5, 3, 4, 1]
    assert transform_list(list_input) == list_target


def test_popMiddle_1():
    list1 = [1, 5, 6, 7, 8]
    target = [1, 5, 7, 8]
    assert pop_middle(list1) == target


def test_popMiddle_2():
    list1 = [5, 0, 6, 7, 8, 3, 4]
    target = [5, 0, 6, 8, 3, 4]
    assert pop_middle(list1) == target


def test_popMiddle_3():
    list1 = [1, 5, 6, 7, 8, 24, 567, 5, 2, 4, 3]
    target = [1, 5, 6, 7, 8, 567, 5, 2, 4, 3]
    assert pop_middle(list1) == target
