# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        n, tail = 1, head
        while tail.next:
            tail = tail.next
            n += 1
        
        k %= n
        if k == 0:
            return head

        tail.next = head

        steps_to_tail = n - k - 1
        new_tail = head

        for i in range(steps_to_tail):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None
        return new_head