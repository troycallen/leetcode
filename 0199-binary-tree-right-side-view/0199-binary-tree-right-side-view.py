class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque([root])

        right_side = []

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                if i == level_size - 1:
                    right_side.append(node.val)
                

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
                
        return right_side
        

            
            