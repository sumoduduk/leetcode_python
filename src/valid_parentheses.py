class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0 or len(s) == 0:
            return False

        char_dict = {"(": ")", "{": "}", "[": "]"}
        arr = []

        for char in s:
            if char in char_dict.keys():
                arr.append(char)
            else:
                lent = len(arr)
                if lent == 0:
                    return False
                if char_dict[arr[lent - 1]] == char:
                    arr.pop()
                else:
                    return False

        return len(arr) == 0


# print(Solution().isValid("([)]"))

# ")": "(", "}": "{", "]": "["


def test_parentheses1():
    input = "()"
    target = True
    sol = Solution()

    assert sol.isValid(input) == target


def test_parentheses2():
    input = "()[]{}"
    target = True
    sol = Solution()

    assert sol.isValid(input) == target


def test_parentheses3():
    input = "(]"
    target = False
    sol = Solution()

    assert sol.isValid(input) == target


def test_parentheses4():
    input = "([)]"
    target = False
    sol = Solution()

    assert sol.isValid(input) == target


def test_parentheses5():
    input = "{[]}"
    target = True
    sol = Solution()

    assert sol.isValid(input) == target


def test_parentheses6():
    input = "){"
    target = False
    sol = Solution()

    assert sol.isValid(input) == target


def test_parentheses7():
    input = "(])"
    target = False
    sol = Solution()

    assert sol.isValid(input) == target
