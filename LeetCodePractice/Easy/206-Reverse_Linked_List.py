# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None

        prev = None
        current = head
        next_node = current.next
        while current is not None:
            current.next = prev
            prev = current
            current = next_node
            if current is not None:
                next_node = current.next

        return prev

b1 = ListNode(1)
b2 = ListNode(2)
b3 = ListNode(3)
b1.next = b2
b2.next = b3

result_node2 = Solution().reverseList(b1)
print(result_node2.val if result_node2 else [])
