# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        q = deque([root])

        while q:
            # Could do this instead:
            row_max = float('-inf')  # or don't initialize at all
            n = len(q)
            for i in range(n):
                node = q.popleft()
                row_max = max(row_max, node.val)  # This would work for first value too
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(row_max)
        return res
