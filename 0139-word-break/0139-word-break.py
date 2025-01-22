class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # Convert wordDict to a set for faster lookup
        wordSet = set(wordDict)

        # Initialize memoization cache
        memo = {}

        def dfs(start: int) -> bool:

            # If we've reached the end of the string, return True
            if start == len(s):
                return True

            # If this subproblem has been solved before, return the cached result
            if start in memo:
                return memo[start]

            # Try all possible word lengths from this starting position
            for end in range(start + 1, len(s) + 1):

                # Check if the current substring is in wordSet and the rest can be segmented
                if s[start:end] in wordSet and dfs(end):
                    memo[start] = True
                    return True

            # If no valid segmentation found, memoize and return False
            memo[start] = False
            return False

        # Start the recursive process from the beginning of the string
        return dfs(0)