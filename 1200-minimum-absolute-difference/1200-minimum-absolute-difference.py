class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        min_diff = float('inf')

        res = []

        for i in range(1, len(arr)):
            prev = arr[i-1]
            curr = arr[i]
            curr_diff = curr - prev

            if curr_diff < min_diff:
                min_diff = curr_diff
                res = [[prev, curr]]
            

            elif curr_diff == min_diff:
                res.append([prev,curr])

        return res