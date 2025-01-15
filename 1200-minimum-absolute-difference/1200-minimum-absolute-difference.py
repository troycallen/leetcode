class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float('inf')

        diffs = defaultdict(list)

        for i in range(1, len(arr)):
            curr_diff = arr[i] - arr[i-1]
            diffs[curr_diff].append([arr[i-1], arr[i]])
            min_diff = min(min_diff, curr_diff)
        
        return diffs[min_diff]