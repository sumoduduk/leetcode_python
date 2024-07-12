from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictComplement = {}
        numLen = len(nums)

        for i in range(numLen):

            if nums[i] in dictComplement:
                return [dictComplement[nums[i]], i]
            else:
                complement = target - nums[i]
                dictComplement[complement] = i
        return [0, 0]


def test_twoSum_1():
    nums = [2, 7, 11, 5]
    target = 9
    solution = Solution()
    res = solution.twoSum(nums, target)
    assert res == [0, 1]


def test_twoSum_2():
    nums = [3, 2, 4]
    target = 6
    solution = Solution()
    res = solution.twoSum(nums, target)
    assert res == [1, 2]


def test_twoSum_3():
    nums = [3, 3]
    target = 6
    solution = Solution()
    res = solution.twoSum(nums, target)
    assert res == [0, 1]
