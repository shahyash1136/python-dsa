class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def _get_length(self):
        temp = self.head
        length = 0
        if temp is not None:
            length += 1
            temp = temp.next
        return length

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

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp

    def insert_at_index(self, index, value):
        length = self._get_length()
        if index > length:
            raise IndexError("Index out of bound")
        elif index == 0:
            return self.prepend(value)
        elif index == length:
            return self.append(value)
        else:
            new_node = Node(value)
            current = self.head
            for _ in range(index):
                current = current.next

            new_node.next = current
            new_node.prev = current.prev
            current.prev.next = new_node
            current.prev = new_node

    def shift(self):
        if self.head is None:
            raise IndexError("Index out of bound")
        temp = self.head
        if self.head.next is None:
            self.head = None
        else:
            temp.next.prev = None
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
            current = self.head
            for _ in range(index):
                current = current.next

            current.next.prev = current.prev
            current.prev.next = current.next
            current.prev = None
            current.next = None
            return current

    def traverse_forward(self):
        if self.head is None:
            return
        else:
            temp = self.head
            while temp is not None:
                print(temp.val)
                temp = temp.next

    def traverse_backward(self):
        if self.head is None:
            return
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next

            while temp is not None:
                print(temp.val)
                temp = temp.prev
