class Solution:
    def flatten(self, head: "Optional[Node]") -> "Optional[Node]":
        if head is None:
            return None
        else:
            stack = []
            current = head
            while current is not None:
                if current.child is not None:
                    if current.next is not None:
                        stack.append(current.next)
                    current.next = current.child
                    current.child.prev = current
                    current.child = None
                if current.next is None and len(stack) > 0:
                    pop_node = stack.pop()
                    current.next = pop_node
                    pop_node.prev = current

                current = current.next
            return head
