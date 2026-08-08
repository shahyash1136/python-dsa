class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_lines(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def _handle_empty_list(self, new_node):
        self.head = new_node
        self.tail = new_node

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
        prev_node = self.head
        for _ in range(index - 1):
            prev_node = prev_node.next

        new_node.next = prev_node.next
        prev_node.next = new_node

        self.length += 1


myLinkedList1 = LinkedList()
myLinkedList1.append(2)
myLinkedList1.append(4)
myLinkedList1.append(5)
myLinkedList1.insert_at_index(1, 3)
myLinkedList1.print_lines()
