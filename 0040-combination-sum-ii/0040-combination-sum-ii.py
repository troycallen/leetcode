class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, cur , total):
            if total == target:
                # make a copy so not reference
                res.append(cur.copy())
                return

            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i + 1, cur, candidates[i] + total)
            cur.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i = i + 1
            
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        return res