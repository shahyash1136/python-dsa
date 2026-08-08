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
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

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


myLinkedList = LinkedList()
myLinkedList.prepend(2)
myLinkedList.print_lines()
