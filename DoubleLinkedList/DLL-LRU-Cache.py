class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hashMap = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_tail(self, node):
        current = self.tail
        node.next = current
        node.prev = current.prev
        current.prev.next = node
        current.prev = node

    def get(self, key):
        if key not in self.hashMap:
            return -1
        else:
            node = self.hashMap[key]
            self._remove(node)
            self._add_to_tail(node)
            return node.value

    def put(self, key, value):
        if key in self.hashMap:
            node = self.hashMap[key]
            node.value = value
            self._remove(node)
            self._add_to_tail(node)
        else:
            if len(self.hashMap) == self.capacity:
                node = self.head.next
                self._remove(node)
                del self.hashMap[node.key]
            new_node = Node(key, value)
            self.hashMap[key] = new_node
            self._add_to_tail(new_node)
