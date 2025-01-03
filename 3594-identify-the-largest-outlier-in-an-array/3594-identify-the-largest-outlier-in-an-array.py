class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        largest = float('-inf')

        num_counts = Counter(nums)

        for i in num_counts:
            #print(i)
            potential_ol = total_sum - (2 * i)

            if potential_ol in num_counts:
                if potential_ol != i or num_counts[i] > 1:
                    largest = max(largest, potential_ol)

        return largest
