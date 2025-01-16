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
        
        curr = None
        prev = None

        stack = [head]

        while stack:
            curr = stack.pop()

            if prev:
                curr.prev = prev
                prev.next = curr
            
            if curr.next:
                stack.append(curr.next)

            if curr.child:
                stack.append(curr.child)
                curr.child = None
            
            prev = curr

        return head
            
                


