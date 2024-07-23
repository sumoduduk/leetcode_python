from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def assign_list(arr: List[int]) -> ListNode:
    tail = ListNode(arr[len(arr) - 1])
    for i in arr[-2::-1]:
        tail.next = tail.val
        tail = ListNode(i)
    return tail


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        curr = list1
        curr2 = list2
        while curr and curr2:
            curr = curr.next
            curr2 = curr2.next

    # def test_mergeTwoList_1():


input = ListNode(1, ListNode(2, ListNode(4)))
input2 = ListNode(1, ListNode(3, ListNode(4)))

# print(ListNode(1, ListNode(2)).val)

Solution().mergeTwoLists(input, input2)
#
arr = [1, 1, 2, 3, 4, 4]
target = assign_list(arr)

curr = target
while curr:
    print(curr.val)
    curr = curr.next
print(curr)
#
#     sol = Solution()
#     assert sol.mergeTwoLists(input, input2) == target
