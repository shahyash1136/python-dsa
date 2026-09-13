from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None

        slow = head
        fast = head.next

        while fast is not None:
            if slow.val == fast.val:
                slow.next = fast.next
            else:
                slow = fast
            fast = slow.next

        return head


head = ListNode(
    1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4))))))
)
solution = Solution()
values = solution.deleteDuplicates(head)

result = []
while values is not None:
    result.append(values.val)
    values = values.next
print(result)
