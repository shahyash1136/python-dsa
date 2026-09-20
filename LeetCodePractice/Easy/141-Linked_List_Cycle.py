from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            if slow is fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False


n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(0)
n4 = ListNode(-4)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n2  # cycle: -4 points back to the node with value 2

head = n1
solution = Solution()
print(solution.hasCycle(head))  # expected: True
