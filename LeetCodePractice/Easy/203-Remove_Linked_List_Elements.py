# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        if head is None:
            return None
        while head is not None and head.val == val:
            head = head.next
        prev = head
        temp = head
        while temp is not None:
            if temp.val == val:
                prev.next = temp.next
            else:
                prev = temp
            temp = prev.next

        return head


b1 = ListNode(7)
b2 = ListNode(7)
b3 = ListNode(7)
b4 = ListNode(7)
b5 = ListNode(7)
b6 = ListNode(7)
b7 = ListNode(7)
b1.next = b2
b2.next = b3
b3.next = b4
b4.next = b5
b5.next = b6
b6.next = b7

result_node2 = Solution().removeElements(b1, 7)
print(result_node2.val if result_node2 else [])  # expected: None
