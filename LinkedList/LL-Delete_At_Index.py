class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def _handel_empty_list(self, new_node):
        self.head = new_node
        self.tail = new_node

    def _get_prev_node(self, index):
        prev_node = self.head
        for _ in range(index - 1):
            prev_node = prev_node.next
        return prev_node

    def print_lines(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            self._handel_empty_list(new_node)
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self._handel_empty_list(new_node)
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1

    def insert_at_index(self, index, value):
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        if index > self.length:
            raise IndexError("Index out of bound")

        new_node = Node(value)

        prev_node = self._get_prev_node(index)

        new_node.next = prev_node.next
        prev_node.next = new_node

        self.length += 1

    def delete_at_index(self, index):
        if index == 0:
            prev = self.head
            self.head = prev.next
            prev.next = None
            self.length -= 1
            return
        if index == self.length - 1:
            prev = self._get_prev_node(index)
            self.tail = prev
            prev.next = None
            self.length -= 1
            return
        if index >= self.length:
            raise IndexError("Index out of bound")

        prev = self._get_prev_node(index)
        prev.next = prev.next.next

        self.length -= 1


myLinkedList1 = LinkedList()
myLinkedList1.append(2)
myLinkedList1.append(3)
myLinkedList1.append(4)
myLinkedList1.append(5)
# myLinkedList1.insert_at_index(1, 3)
print(f"Before Deleting the length = {myLinkedList1.length}")
myLinkedList1.delete_at_index(3)
myLinkedList1.print_lines()
print(f"After Deleting the length = {myLinkedList1.length}")
myLinkedList1.length
