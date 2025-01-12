class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        # Helper function to calculate power value
        def get_power(x):
            steps = 0
            num = x
            while num != 1:
                if num % 2 == 0:
                    num = num // 2
                else:
                    num = 3 * num + 1
                steps += 1
            return steps
        
        # Create list of (power_value, original_number) pairs
        power_pairs = []
        for num in range(lo, hi + 1):
            power = get_power(num)
            power_pairs.append((power, num))
        
        # Sort by power value first, then by number
        power_pairs.sort()
        
        # Return kth number (k is 1-indexed)
        return power_pairs[k-1][1]