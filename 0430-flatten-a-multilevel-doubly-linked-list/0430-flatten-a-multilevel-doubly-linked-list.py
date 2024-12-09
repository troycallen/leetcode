"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Initialize stack and dummy node
        stack = []
        dummy = Node(0, None, head, None)
        curr = dummy
        stack.append(head)

        # Iterate through the stack
        while stack:
            node = stack.pop()

            # Connect current node to the flattened list
            curr.next = node
            node.prev = curr

            # Push next node to stack if exists
            if node.next:
                stack.append(node.next)

            # Push child node to stack if exists
            if node.child:
                stack.append(node.child)
                node.child = None

            # Move current pointer
            curr = node

        # Disconnect dummy node from the list
        dummy.next.prev = None

        return dummy.next
