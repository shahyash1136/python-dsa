class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def _handle_empty_list(self,new_node):
        self.head = new_node


    def _get_length(self):
        temp = self.head
        length = 0
        while temp is not None:
            length += 1
            temp = temp.next

        return length

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = self._handle_empty_list(new_node)
        else:
            temp= self.head
            while temp.next is not None:
                temp = temp.next

            temp.next = new_node

    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = self._handle_empty_list(new_node)
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_index(self,index,value):
        length = self._get_length()
        if index > length:
            raise IndexError("Index out of bound")
        elif index == 0:
            return self.prepend()
        elif index == length:
            return self.append()
        else:
            new_node = Node(value)
            prev_node = self.head
            for _ in range(index - 1):
                prev_node = prev_node.next

            new_node.next = prev_node.next
            prev_node.next = new_node

    def pop(self):
        pass

    def shift(self):
        pass

    def delete_at_index(self,index):
        pass

    def delete_at_value(self):
        pass

    def reverse(self):
        pass

    def find_middle(self):
        pass
    def has_cycle(self):
        pass
    def nth_from_end(self, n):
        pass
    def rotate_nth_time(self, n):
        pass
    def merge_two_sorted_lists(self, a_list, b_list):
        pass
    def remove_duplicate(self):
        pass
    def is_palindrome(self):
        pass
    def remove_elements(self, val):
        pass
