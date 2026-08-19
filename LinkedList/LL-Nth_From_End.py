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

    def _get_length(self):
        temp = self.head
        length = 0
        while temp is not None:
            length += 1
            temp = temp.next
        return length

    def _handle_empty_node(self, new_node):
        self.head = new_node

    def _get_prev_node(self, index):
        prev_node = self.head
        for _ in range(index - 1):
            prev_node = prev_node.next
        return prev_node

    def append(self, val):
        new_node = Node(val)
        if self.head is None:
            self._handle_empty_node()
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next

            temp.next = new_node

    def prepend(self, val):
        new_node = Node(val)
        if self.head is None:
            self._handle_empty_node(new_node)
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

        new_node = Node(val)
        prev_node = self._get_prev_node(index)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def pop(self):
        if self.head is None:
            return None
        else:
            temp = self.head
            prev_node = self.head
            while temp.next is not None:
                prev_node = temp
                temp = temp.next

            prev_node.next = None
            return temp

    def shift(self):
        if self.head is None:
            return None
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
            return None
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
            return False
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
        pass

    def has_cycle(self):
        pass

    def nth_from_end(self, n):
        pass


myLinkedList = LinkedList()
myLinkedList.prepend(10)
myLinkedList.prepend(5)
myLinkedList.append(20)
myLinkedList.insert_at_index(2, 15)
myLinkedList.print_lines()


print(f"Delete called here => {myLinkedList.delete_by_value(30)}")
myLinkedList.print_lines()
