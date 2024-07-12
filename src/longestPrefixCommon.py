from typing import List, Tuple


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        word_1 = strs.pop(0)
        char_1: List[str] = list(word_1)

        len_char1 = len(word_1)
        if len_char1 == 0:
            return ""
        tuples_char: List[Tuple[str, int]] = list(map(lambda x: (x, 1), char_1))

        for word in strs:
            if len(word) == 0:
                tuples_char = [("a", 0)]
                break
            elif len(word) == 1 and !(word in char_1):
                tuples_char = [("a", 0)]
                break
            for i, char in enumerate(word):
                if i == len_char1:
                    break
                else:
                    # print(f"char = {char}")
                    char_target = char_1[i]
                    if char == char_target:
                        num_tuple = tuples_char[i][1] + 1
                        tuples_char[i] = (char_target, num_tuple)
                    else:
                        num_tuple = 0
                        tuples_char[i] = (char_target, num_tuple)
                        break

        print(f"Tuple {tuples_char}")
        first_tupel = tuples_char.pop(0)
        value = first_tupel[1]
        list_target: List[str] = [char_1[0]]

        if value > 1:
            for char_, val in tuples_char:
                if val == value:
                    list_target.append(char_)

            return "".join(list_target)
        else:
            return ""


def test_longestCommonPrefix_1():
    strs = ["flower", "flow", "flight"]
    target = "fl"
    sol = Solution()
    assert sol.longestCommonPrefix(strs) == target


def test_longestCommonPrefix_2():
    strs = ["dog", "racecar", "car"]
    target = ""
    sol = Solution()
    assert sol.longestCommonPrefix(strs) == target


def test_longestCommonPrefix_3():
    strs = ["a"]
    target = "a"
    sol = Solution()
    assert sol.longestCommonPrefix(strs) == target


def test_longestCommonPrefix_5():
    strs = ["aabdlddwekdjakdjwek"]
    target = "aabdlddwekdjakdjwek"
    sol = Solution()
    assert sol.longestCommonPrefix(strs) == target


def test_longestCommonPrefix_4():
    strs = [""]
    target = ""
    sol = Solution()
    assert sol.longestCommonPrefix(strs) == target


def test_longestCommonPrefix_7():
    strs = ["flower", "flower", "flower", "flower"]
    target = "flower"
    sol = Solution()
    assert sol.longestCommonPrefix(strs) == target


def test_longestCommonPrefix_8():
    strs = ["cir", "car"]
    target = "c"
    sol = Solution()
    assert sol.longestCommonPrefix(strs) == target


def test_longestCommonPrefix_9():
    strs = ["aa", "aa"]
    target = "aa"
    sol = Solution()
    assert sol.longestCommonPrefix(strs) == target


def test_longestCommonPrefix_10():
    strs = ["a", "a", "b"]
    target = ""
    sol = Solution()
    assert sol.longestCommonPrefix(strs) == target


def test_longestCommonPrefix_11():
    strs = ["abab", "aba", ""]
    target = ""
    sol = Solution()
    assert sol.longestCommonPrefix(strs) == target


def test_longestCommonPrefix_12():
    strs = ["c", "acc", "ccc"]
    target = ""
    sol = Solution()
    assert sol.longestCommonPrefix(strs) == target


def test_longestCommonPrefix_13():
    strs = ["cc", "ccc", "cccc"]
    target = "cc"
    sol = Solution()
    assert sol.longestCommonPrefix(strs) == target


def test_longestCommonPrefix_14():
    strs = ["aba", "c", "b", "a", "ab"]
    target = ""
    sol = Solution()
    assert sol.longestCommonPrefix(strs) == target


def test_longestCommonPrefix_15():
    strs = ["ab", "a"]
    target = "a"
    sol = Solution()
    assert sol.longestCommonPrefix(strs) == target
