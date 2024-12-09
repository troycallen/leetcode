class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        window = set()
        longest = 0

        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])     # remove the left val and increment l pointer
                l += 1                  # to remove all of it
            
            window.add(s[r])
            longest = max(longest, r-l+1)
        return longest