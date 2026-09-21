from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        slow = headA
        fast = headB

        while True:
            if slow is fast:
                return fast
            else:
                slow = headB if slow is None else slow.next
                fast = headA if fast is None else fast.next


# --- Case 1: Intersecting lists ---
# Shared/common part (same node objects, will appear in both lists)
c1 = ListNode(8)
c2 = ListNode(4)
c3 = ListNode(5)
c1.next = c2
c2.next = c3
# c3.next = None (end)

# List A: 4 -> 1 -> [8 -> 4 -> 5]
a1 = ListNode(4)
a2 = ListNode(1)
a1.next = a2
a2.next = c1  # <-- yahi se intersection shuru hota hai

# List B: 5 -> 6 -> 1 -> [8 -> 4 -> 5]
b1 = ListNode(5)
b2 = ListNode(6)
b3 = ListNode(1)
b1.next = b2
b2.next = b3
b3.next = c1  # <-- same node c1, intersection yahin se

headA = a1
headB = b1

result_node = Solution().getIntersectionNode(headA, headB)
print(result_node.val if result_node else None)  # expected: 8


# --- Case 2: Non-intersecting lists ---
x1 = ListNode(2)
x2 = ListNode(6)
x3 = ListNode(4)
x1.next = x2
x2.next = x3

y1 = ListNode(1)
y2 = ListNode(5)
y1.next = y2
# koi shared node nahi

result_node2 = Solution().getIntersectionNode(x1, y1)
print(result_node2.val if result_node2 else None)  # expected: None
