class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def pop(self):
        if self.length == 0:
            return None

        temp = self.head
        prev = self.head

        while temp.next is not None:
            prev = temp
            temp = temp.next

        self.tail = prev
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp


my_linkedList = LinkedList(1)
my_linkedList.append(2)
my_linkedList.append(3)
print("Complete List")
my_linkedList.print_list()
my_linkedList.pop()
print("single value removed")
my_linkedList.print_list()
