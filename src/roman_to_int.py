class Solution:
    def romanToInt(self, s: str) -> int:

        result = 0
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        mapped_list = list(map(lambda x: roman_dict[x], s))
        temp = 0
        nums = mapped_list[::-1]

        for num in nums:
            if num >= result:
                result += num
            else:
                if temp == num:
                    result += num
                else:
                    result -= num
            temp = num

        return result


def test_roman_1():
    s = "III"
    # 914
    # cmxiv
    # vixmc
    # 5, 1, 10, 1000, 100
    # result 914
    # temp 1000
    target = 3
    sol = Solution()
    assert sol.romanToInt(s) == target


def test_roman_2():

    # 58
    # IIIVL
    # 1, 1, 1, 5, 50
    s = "LVIII"
    # temp 50
    # result 58
    target = 58
    sol = Solution()
    assert sol.romanToInt(s) == target


def test_roman_3():

    # vicxmcm
    # 5, 1, 100, 10, 1000, 100, 1000
    # 1994
    s = "MCMXCIV"
    target = 1994
    sol = Solution()
    assert sol.romanToInt(s) == target
