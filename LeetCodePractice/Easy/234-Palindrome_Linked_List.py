# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def findMiddle(self, node: ListNode | None):
        slow = node
        fast = node
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverseList(self, node: ListNode | None):
        prev = None
        current = node
        next_node = current.next
        while current is not None:
            current.next = prev
            prev = current
            current = next_node
            if current is not None:
                next_node = current.next

        return prev

    def isPalindrome(self, head: ListNode | None) -> bool:
        if head is None:
            return False

        middleValue = self.findMiddle(head)
        reverseList = self.reverseList(middleValue)
        temp = head
        while temp is not None and reverseList is not None:
            if temp.val == reverseList.val:
                temp = temp.next
                reverseList = reverseList.next
            else:
                return False
        return True


b1 = ListNode(1)
# b2 = ListNode(2)
# b3 = ListNode(3)
# b4 = ListNode(4)
# b5 = ListNode(5)
# b6 = ListNode(6)
# b1.next = b2
# b2.next = b3
# b3.next = b4
# b4.next = b5
# b5.next = b6

result_node2 = Solution().isPalindrome(b1)
print(result_node2)
