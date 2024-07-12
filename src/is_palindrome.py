from typing import List


class Solution:
    def isPalindrome(self, x: int) -> bool:

        def transform_list(x: List[str]) -> List[str]:

            for i in range(len(x)):
                last = x.pop()
                x.insert(i, last)

            return x

        def extract_list(arr: List[str]) -> bool:
            list1 = arr[: len(arr) // 2]
            list2 = arr[len(arr) // 2 :]
            new_list = transform_list(list2)
            return list1 == new_list

        if x >= 0:
            digits = [char for char in str(x)]
            digit_len = len(digits)
            if digit_len % 2 == 0:
                return extract_list(digits)
            else:
                digits.pop(digit_len // 2)
                return extract_list(digits)
        return False


def test_isPalindrome_1():
    x = 121
    output = True
    solution = Solution()
    assert solution.isPalindrome(x) == output


def test_isPalindrome_2():
    x = -121
    output = False
    solution = Solution()
    assert solution.isPalindrome(x) == output


def test_isPalindrome_3():
    x = 10
    output = False
    solution = Solution()
    assert solution.isPalindrome(x) == output
