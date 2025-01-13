class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                # have to make a copy so we dont mess with it in later recursions
                res.append(cur.copy())
                return
            
            if total > target or i >= len(nums):
                # if we are out of bounds or too large of a sum
                return

            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            # have to pop before we go right in the decision tree
            cur.pop()
            # cur is now the same as before so we just change i 
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        return res
            

