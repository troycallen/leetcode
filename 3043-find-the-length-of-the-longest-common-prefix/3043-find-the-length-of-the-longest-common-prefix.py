class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        common = defaultdict(int)
        longest = 0

        for num in arr1:
            str_num = str(num)
            prefix = ""
            for ch in str_num:
                prefix += ch
                common[prefix] += 1
        
        for num in arr2:
            str_num = str(num)
            prefix = ""
            for ch in str_num:
                prefix += ch
                if prefix in common:
                    longest = max(longest, len(prefix))
        
        return longest