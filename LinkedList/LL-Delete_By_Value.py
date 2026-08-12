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
        curr = self.head
        while curr is not None:
            print(curr.value)
            curr = curr.next

    def _handle_empty_list(self, new_node):
        self.head = new_node
        self.tail = new_node

    def _get_prev_node(self, index):
        prev = self.head
        for _ in range(index - 1):
            prev = prev.next
        return prev

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
        elif index >= self.length:
            raise IndexError("Index out of bound")

        new_node = Node(value)
        prev = self._get_prev_node(index)

        new_node.next = prev.next
        prev.next = new_node
        self.length += 1

    def delete_at_index(self, index):
        if index >= self.length:
            raise IndexError("Index out of bound")
        elif index == 0:
            prev = self.head
            self.head = prev.next
            prev.next = None
            self.length -= 1
            return
        elif index == self.length - 1:
            prev = self._get_prev_node(index)
            self.tail = prev
            prev.next = None
            self.length -= 1
            return

        prev = self._get_prev_node(index)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        pass

    def delete_by_value(self, value):
        if self.head.value == value:
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.length -= 1
            return
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
            return


myLinkedList1 = LinkedList()
myLinkedList1.append(2)
myLinkedList1.append(3)
myLinkedList1.append(4)
myLinkedList1.append(5)
# myLinkedList1.insert_at_index(1, 3)
print(f"Before Deleting the length = {myLinkedList1.length}")
# myLinkedList1.delete_at_index(3)
myLinkedList1.delete_by_value(6)
myLinkedList1.print_lines()
print(f"After Deleting the length = {myLinkedList1.length}")
myLinkedList1.length
