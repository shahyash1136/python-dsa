class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def pop(self):
        if self.head is None:
            raise IndexError("Index out of bound")
        elif self.head.next is None:
            temp = self.head
            self.head = None
            return temp
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next

            temp.prev.next = None
            temp.prev = None
            return temp

    def prepend(self, val):
        new_node = Node(val)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node