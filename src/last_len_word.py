class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0
        chars = list(s)
        len_chars = len(s)

        for i in range(len_chars - 1, -1, -1):

            current_char = chars[i]
            if current_char == " ":
                if counter == 0:
                    continue
                else:
                    break
            else:
                counter += 1

        return counter


def test_lenLast_1():
    s = "   fly me   to   the moon  "
    target = 4
    sol = Solution()
    assert sol.lengthOfLastWord(s) == target


def test_lenLast_2():
    s = "luffy is still joyboy"
    target = 6
    sol = Solution()
    assert sol.lengthOfLastWord(s) == target
