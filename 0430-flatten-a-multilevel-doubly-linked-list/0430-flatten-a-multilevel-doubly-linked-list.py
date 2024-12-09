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

        # Initialize variables
        stack = [head]
        prev = None
        curr = None

        # We set first var in stack to be the head so we can instantly pop 

        # Iterate through the stack
        while stack:
            # Pop the current node from the stack
            curr = stack.pop()

            # Connect the previous node to the current node
            if prev:
                prev.next = curr
                curr.prev = prev

            # Push the next node to the stack if it exists
            if curr.next:
                stack.append(curr.next)

            # Push the child node to the stack if it exists
            if curr.child:
                stack.append(curr.child)
                curr.child = None

            # Move to the next node
            prev = curr

        return head
