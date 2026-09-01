def palindrome(self):
    if self.head is None:
        return False
    elif self.head.next is None:
        return True
    else:
        backward = self.head
        while backward.next is not None:
            backward = backward.next
        forward = self.head

        while forward is not backward and forward.prev is not backward:
            if forward.val == backward.val:
                forward = forward.next
                backward = backward.prev
            else:
                return False
        return True
        
