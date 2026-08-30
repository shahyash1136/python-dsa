class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def prepend(self, val):
        new_node = Node(val)
        new_node.next = self.head
        if self.head is None:
            self.tail = new_node
        else:
            self.head.prev = new_node
        self.head = new_node
        self.length += 1

    def append(self, val):
        new_node = Node(val)
        new_node.prev = self.tail
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def insert_at_index(self, index, val):
        if index > self.length:
            raise IndexError("Index out of bound")
        elif index == 0:
            return self.prepend(val)
        elif index == self.length:
            return self.append(val)
        else:
            new_node = Node(val)
            current = self.head
            for _ in range(index):
                current = current.next

            new_node.next = current
            new_node.prev = current.prev
            current.prev.next = new_node
            current.prev = new_node
            self.length += 1

    def pop(self):
        if self.head is None:
            raise IndexError("Index out of bound")
        elif self.head.next is None:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        else:
            temp = self.tail
            temp.prev.next = None
            self.tail = temp.prev
            temp.prev = None
            self.length -= 1
            return temp

    def shift(self):
        if self.head is None:
            raise IndexError("Index out of bound")
        elif self.head.next is None:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.head.prev = None
            self.length -= 1
            return temp

    def delete_at_index(self, index):
        if index >= self.length:
            raise IndexError("Index out of bound")
        elif index == 0:
            return self.shift()
        elif index == self.length - 1:
            return self.pop()
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            current.prev.next = current.next
            current.next.prev = current.prev
            current.next = None
            current.prev = None
            self.length -= 1
            return current

    def traverse_forward(self):
        if self.head is None:
            return
        else:
            temp = self.head
            while temp is not None:
                print(temp.value)
                temp = temp.next

    def traverse_backward(self):
        if self.head is None:
            return
        else:
            temp = self.tail
            while temp is not None:
                print(temp.value)
                temp = temp.prev

    def reverse_dll(self):
        if self.head is None:
            return
        else:
            temp = self.head
            current = self.head
            next = current.next
            while current is not None:
                current.next = current.prev
                current.prev = next
                current = next
                if current is not None:
                    next = current.next

            self.head = self.tail
            self.tail = temp
