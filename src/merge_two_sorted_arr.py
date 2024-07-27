from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        """
        a = m - 1
        b = n - 1
        c = m + n - 1

        while b >= 0:

            if nums1[a] < nums2[b]:
                nums1[c] = nums2[b]
                b = b - 1
            else:
                nums1[c] = nums1[a]
                nums1[a] = nums2[b]
                a = a - 1

            c = c - 1


def test_sorted_array1():
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m = 3
    n = 3
    target = [1, 2, 2, 3, 5, 6]
    sol = Solution()
    sol.merge(nums1, m, nums2, n)
    assert nums1 == target


def test_sorted_array2():
    nums1 = [0]
    nums2 = [1]
    m = 0
    n = 1
    target = [1]
    sol = Solution()
    sol.merge(nums1, m, nums2, n)
    assert nums1 == target
