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

    def _get_prev_node(self,index):
        prev_node = self.head
        for _ in range(index - 1):
            prev_node = prev_node.next
        return prev_node

    def _reverse(self,middle_element):
        prev= None
        current = middle_element.next
        next = current.next
        while current is not None:
            current.next = prev
            prev = current
            current = next
            if current is not None:
                next = current.next

        return current

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
            return self.prepend(value)
        elif index == length:
            return self.append(value)
        else:
            new_node = Node(value)
            prev_node = self._get_prev_node(index)

            new_node.next = prev_node.next
            prev_node.next = new_node

    def pop(self):
        if self.head is None:
            raise IndexError("List is empty")
        elif self.head.next is None:
            temp = self.head
            self.head = None
            return temp
        else:
            temp = self.head
            prev_node = self.head
            while temp.next is not None:
                prev_node = temp
                temp = prev_node.next

            prev_node.next = None
            return temp

    def shift(self):
        if self.head is None:
            return None
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
            return temp

    def delete_at_index(self,index):
        length = self._get_length()
        if index >= length:
            raise IndexError("Index out of bound")
        elif index == 0:
            return self.shift()
        elif index == length - 1:
            return self.pop()
        else:
            prev_node = self._get_prev_node(index)
            temp = prev_node.next
            prev_node.next = temp.next
            temp.next = None
            return temp

    def delete_at_value(self,value):
        if self.head is None:
            raise IndexError("Index out of bound")
        elif self.head.value == value:
            return self.shift()
        else:
            temp = self.head 
            prev = self.head
            while temp is not None and temp.value != value:
                prev = temp
                temp = prev.next

            if temp is None:
                return

            prev.next = temp.next
            temp.next = None
            return temp

    def reverse(self):
        if self.head is None:
            return None
        else:
            prev = None
            current = self.head
            next = current.next
            while current is not None:
                current.next = prev
                prev = current
                current = next
                if current is not None:
                    next = current.next
            return prev

    def find_middle(self):
        if self.head is not None:
            return
        else:
            slow = self.head
            fast = self.head
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next

            return slow

    def has_cycle(self):
        if self.head is None:
            return False
        else:
            slow = self.head
            fast = self.head
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next

                if slow is fast:
                    return True

            return False

    def nth_from_end(self, n):
        if self.head is None:
            return None
        length = self._get_length()
        if n > length:
            raise IndexError("Index out of bound")

        first = self.head
        second = self.head

        for _ in range(n):
            first = first.next

        while first is not None:
            first = first.next
            second = second.next

        return second

    def rotate_nth_time(self, n):
        if self.head is None:
            return
        length = self._get_length()
        n = n % length
        if n == 0:
            return

        new_tail = self._get_prev_node(length - n)
        new_head = new_tail.next
        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = self.head
        new_tail.next = None
        self.head = new_head

    def merge_two_sorted_lists(self, a_list, b_list):
        dummy = Node(0)
        tail = dummy
        while a_list is not None or b_list is not None:
            if a_list is None:
                tail.next = b_list
                b_list = b_list.next
            elif b_list is None:
                tail.next = a_list
                a_list = a_list.next
            else:
                if a_list.value < b_list.value:
                    tail.next = a_list
                    a_list = a_list.next
                else:
                    tail.next = b_list
                    b_list= b_list.next

            tail = tail.next
        self.head = dummy.next
        return dummy.next

    def remove_duplicate(self):
        if self.head is None:
            return None
        else:
            current = self.head
            while current is not None and current.next is not None:
                if current.value == current.next.value:
                    current.next = current.next.next
                else:
                    current = current.next
            return current

    def is_palindrome(self,node):
        if self.head is None:
            return False
        else:
            middle_element = self.find_middle(node)
            reverse_second_half = self._reverse(middle_element.next)

            start = self.head

            while start.next is not None and reverse_second_half.next is not None:
                if middle_element.value == reverse_second_half.value:
                    start = start.next
                    reverse_second_half = reverse_second_half.next
            return False
        return True

    def remove_elements(self, val):
        pass
