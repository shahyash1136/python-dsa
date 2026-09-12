from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy

        while list1 is not None or list2 is not None:
            if list1 is None:
                temp.next = list2
                list2 = list2.next
            elif list2 is None:
                temp.next = list1
                list1 = list1.next
            else:
                if list1.val < list2.val:
                    temp.next = list1
                    list1 = list1.next
                else:
                    temp.next = list2
                    list2 = list2.next

            temp = temp.next
        self.head = dummy.next
        return dummy.next


a = ListNode()
b = ListNode()
values = Solution().mergeTwoLists(list1=a, list2=b)

result = []
while values is not None:
    result.append(values.val)
    values = values.next
print(result)
