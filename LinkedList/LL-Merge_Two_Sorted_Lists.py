class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_lines(self):
        temp = self.head
        while temp is not None:
            print(temp.val)
            temp = temp.next

    def _handle_empty_list(self, new_node):
        self.head = new_node

    def _get_length(self):
        temp = self.head
        length = 0
        while temp is not None:
            length += 1
            temp = temp.next

        return length

    def _get_prev_node(self, index):
        prev_node = self.head
        for _ in range(index - 1):
            prev_node = prev_node.next

        return prev_node

    def append(self, val):
        new_node = Node(val)
        if self.head is None:
            self._handle_empty_list(new_node)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next

            temp.next = new_node

    def prepend(self, val):
        new_node = Node(val)
        if self.head is None:
            self._handle_empty_list(new_node)
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_index(self, index, val):
        length = self._get_length()
        if index > length:
            raise IndexError("Index out of bound")
        elif index == 0:
            return self.prepend(val)
        elif index == length:
            return self.append(val)
        else:
            new_node = Node(val)
            prev_node = self._get_prev_node(index)

            new_node.next = prev_node.next
            prev_node.next = new_node

    def pop(self):
        if self.head is None:
            raise IndexError("Index out of bound")
        elif self.head.next is None:
            temp = self.head
            self.head = None
            return temp
        else:
            temp = self.head
            prev_node = self.head
            while temp.next is not None:
                prev_node = temp
                temp = prev_node.next

            prev_node.next = None
            return temp

    def shift(self):
        if self.head is None:
            raise IndexError("Index out of bound")
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
            return temp

    def delete_at_index(self, index):
        length = self._get_length()
        if index >= length:
            raise IndexError("Index out of bound")
        elif index == 0:
            return self.shift()
        elif index == length - 1:
            return self.pop()
        else:
            prev_node = self._get_prev_node(index)
            temp = prev_node.next
            prev_node.next = temp.next
            temp.next = None
            return temp

    def delete_by_value(self, val):
        if self.head is None:
            raise IndexError("Index out of bound")
        elif self.head.val == val:
            return self.shift()
        else:
            temp = self.head
            prev = self.head
            while temp is not None and temp.val != val:
                prev = temp
                temp = prev.next

            if temp is None:
                return None

            prev.next = temp.next
            temp.next = None
            return temp

    def reverse(self):
        if self.head is None:
            return None
        else:
            prev = None
            current = self.head
            next = current.next
            while current is not None:
                current.next = prev
                prev = current
                current = next
                if current is not None:
                    next = current.next
            return prev

    def find_middle(self):
        if self.head is None:
            return None
        else:
            slow = self.head
            fast = self.head
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next

            return slow

    def has_cycle(self):
        if self.head is None:
            return False
        else:
            slow = self.head
            fast = self.head
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
                if slow is fast:
                    return True
            return False

    def nth_from_end(self, n):
        length = self._get_length()
        if n > length:
            raise IndexError("Index out of bound")
        elif self.head is None:
            return None
        else:
            first = self.head
            second = self.head
            for _ in range(n):
                first = first.next

            while first is not None:
                first = first.next
                second = second.next

            return second

    def rotate_nth_time(self, n):
        if self.head is None:
            return
        length = self._get_length()
        n = n % length
        if n == 0:
            return

        new_tail = self._get_prev_node(length - n)
        new_head = new_tail.next
        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = self.head
        new_tail.next = None
        self.head = new_head

    def merge_two_sorted_lists(self, a_list, b_list):
        dummy_node = Node(0)
        tail = dummy_node

        while a_list is not None or b_list is not None:
            if a_list is None:
                tail.next = b_list
                b_list = b_list.next
            elif b_list is None:
                tail.next = a_list
                a_list = a_list.next
            else:
                if a_list.val < b_list.val:
                    tail.next = a_list
                    a_list = a_list.next
                else:
                    tail.next = b_list
                    b_list = b_list.next
            tail = tail.next
        self.head = dummy_node.next
        return dummy_node.next


myLinkedList = LinkedList()
myLinkedList.append(30)
myLinkedList.prepend(10)
myLinkedList.append(40)
myLinkedList.insert_at_index(1, 20)

print(myLinkedList.nth_from_end(2).val)
# myLinkedList.print_lines()
