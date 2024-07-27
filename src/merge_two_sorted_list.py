from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def assign_list(arr: List[int]) -> ListNode:
    tail = ListNode(arr[len(arr) - 1])
    head = tail
    for i in arr[-2::-1]:
        head = ListNode(i, head)
    return head


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1

        curr = list1
        curr2 = list2
        target = []

        while curr or curr2:
            if curr and curr2:
                val1 = curr.val
                val2 = curr2.val

                if val1 > val2:
                    target.append(val2)
                    target.append(val1)

                else:
                    target.append(val1)
                    target.append(val2)
                curr = curr.next
                curr2 = curr2.next
            else:

                while curr:
                    target.append(curr.val)
                    curr = curr.next
                while curr2:
                    target.append(curr2.val)
                    curr2 = curr2.next

        target.sort()
        return assign_list(target)


def extract_node(l: Optional[ListNode]):
    curr = l
    while curr:
        print(curr.val)
        curr = curr.next


def test_mergeTwoList_1():
    input1 = ListNode(1, ListNode(2, ListNode(4)))
    input2 = ListNode(1, ListNode(3, ListNode(4)))
    arr = [1, 1, 2, 3, 4, 4]
    target = assign_list(arr)

    sol = Solution()
    result = sol.mergeTwoLists(input1, input2)

    while target and result:
        targetVal = target.val
        resultVal = result.val
        assert targetVal == resultVal

        target = target.next
        result = result.next


def test_mergeTwoList_2():
    input1 = ListNode(5)
    input2 = ListNode(1, ListNode(2, ListNode(4)))
    arr = [1, 2, 4, 5]
    target = assign_list(arr)

    sol = Solution()
    result = sol.mergeTwoLists(input1, input2)

    while target and result:
        targetVal = target.val
        resultVal = result.val
        assert targetVal == resultVal

        target = target.next
        result = result.next


# if list1 == None:
#             return list2
#         elif list2 == None:
#             return list1
#         elif list1 == None and list2 == None:
#             return None
#         elif list1.val <= list2.val:
#                 list1.next = self.mergeTwoLists(list1.next,list2)
#                 return(list1)
#         else:
#             list2.next= self.mergeTwoLists(list1,list2.next)
#             return(list2)
