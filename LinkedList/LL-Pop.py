class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_list(self):
        curr = self.head
        while curr is not None:
            print(curr.value)
            curr = curr.next

    def _handle_empty_list(self, new_node):
        self.head = new_node
        self.tail = new_node

    def _get_prev_node(self, index):
        prev_node = self.head
        for _ in range(index - 1):
            prev_node = prev_node.next
        return prev_node

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self._handle_empty_list(new_node)
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self._handle_empty_list(new_node)
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert_at_index(self, index, value):
        if index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        elif index > self.length:
            raise IndexError("Index out of bound")

        new_node = Node(value)
        prev_node = self._get_prev_node(index)

        new_node.next = prev_node.next
        prev_node.next = new_node

        self.length += 1

    def delete_at_index(self, index):
        if index >= self.length:
            raise IndexError("Index out of bound")
        elif index == 0:
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.length -= 1
            return temp.value
        elif index == self.length - 1:
            temp = self.tail
            prev_node = self._get_prev_node(index)
            self.tail = prev_node
            prev_node.next = None
            self.length -= 1
            return temp.value

        prev_node = self._get_prev_node(index)
        temp = prev_node.next
        prev_node.next = temp.next
        temp.next = None

        self.length -= 1
        return temp.value

    def delete_by_value(self, value):
        if self.head is None:
            return False
        if self.head.value == value:
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.length -= 1
            return temp.value
        else:
            temp = self.head
            prev = self.head
            while temp is not None and temp.value != value:
                prev = temp
                temp = prev.next
            if temp is None:
                return False
            if temp is self.tail:
                self.tail = prev
            prev.next = temp.next
            temp.next = None

            self.length -= 1
            return temp.value

    def pop(self):
        if self.length == 0:
            raise IndexError("List is empty")
        elif self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp.value
        else:
            temp = self.tail
            prev = self._get_prev_node(self.length - 1)
            self.tail = prev
            prev.next = None
            self.length -= 1
            return temp.value

    def pop_without_length(self):
        if self.head is None:
            raise IndexError("List is empty")
        elif self.head.next is None:
            temp = self.head
            self.head = None
            self.tail = None
            return temp.value
        else:
            temp = self.head
            prev = self.head
            while temp.next is not None:
                prev = temp
                temp = prev.next
            self.tail = prev
            prev.next = None
            return temp.value


myLinkedList1 = LinkedList()

myLinkedList1.append(20)
myLinkedList1.prepend(10)
myLinkedList1.insert_at_index(0, 5)
myLinkedList1.insert_at_index(2, 15)
myLinkedList1.insert_at_index(4, 25)
myLinkedList1.append(30)
myLinkedList1.print_list()
# print("=" * 10)
# print(myLinkedList1.delete_at_index(0))
# print("=" * 10)
print("=" * 30)
print(myLinkedList1.delete_by_value(30))
print("=" * 30)
myLinkedList1.print_list()
print("=" * 30)
