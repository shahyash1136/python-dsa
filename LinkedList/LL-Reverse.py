class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_lines(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
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

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
           self.head = self._handle_empty_list(new_node)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self._handle_empty_list(new_node)
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_index(self, index, value):
        length = self._get_length()

        if index == 0:
            return self.prepend(value)
        elif index == length:
            return self.append(value)
        elif index > length:
            raise IndexError("Index out of bound")

        new_node = Node(value)
        prev_node = self._get_prev_node(index)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_at_index(self, index):
        length = self._get_length()

        if index >= length:
            raise IndexError("Index out of bound")
        elif index == 0:
            temp = self.head
            self.head = temp.next
            temp.next = None
            return
        elif index == length - 1:
            prev = self._get_prev_node(index)
            prev.next = None
            return

        prev = self._get_prev_node(index)
        prev.next = prev.next.next
        return

    def delete_by_value(self, value):
        if self.head is None:
            return False
        if self.head.value == value:
            temp = self.head
            self.head = temp.next
            temp.next = None
            return temp.value
        else:
            temp = self.head
            prev = self.head
            while temp is not None and temp.value != value:
                prev = temp
                temp = prev.next

            if temp is None:
                return False
            prev.next = temp.next
            temp.next = None
            return temp.value

    def pop(self):
        if self.head is None:
            raise IndexError("List is empty")
        elif self.head.next is None:
            temp = self.head
            self.head = None
            return temp.value
        else:
            temp = self.head
            prev = self.head
            while temp.next is not None:
                prev = temp
                temp = prev.next

            prev.next = None
            return temp.value

    def shift(self):
        if self.head is None:
            raise IndexError("List is Empty")
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
            return temp.value

    def reverse(self):
        if self.head is None:
            return False

        prev = None
        current = self.head
        next = current.next
        while current is not None:
            current.next = prev
            prev = current
            current = next
            if current is not None:
                next = current.next
        self.tail = self.head
        self.head = prev


myLinkedList = LinkedList()
myLinkedList.append(10)
myLinkedList.append(20)
myLinkedList.prepend(5)
myLinkedList.prepend(0)
myLinkedList.insert_at_index(3, 15)
myLinkedList.print_lines()
myLinkedList.pop()

print("=" * 50)
print(myLinkedList.pop())
print("=" * 50)
myLinkedList.print_lines()
