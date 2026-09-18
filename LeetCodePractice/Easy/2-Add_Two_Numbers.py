# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        dummy = ListNode()
        current = dummy
        carry = 0
        while l1 is not None or l2 is not None:
            val1 = 0 if l1 is None else l1.val
            val2 = 0 if l2 is None else l2.val
            total = val1 + val2 + carry
            current.next = ListNode(total % 10)
            carry = total // 10
            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next
            current = current.next
        if carry > 0:
            current.next = ListNode(carry)
        return dummy.next


l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
solution = Solution()
values = solution.addTwoNumbers(l1, l2)

result = []
while values is not None:
    result.append(values.val)
    values = values.next
print(result)
