class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        
        # Initialize stack with -1 to handle edge cases
        stack = [-1]
        max_length = 0
        
        # Iterate through string
        for i in range(len(s)):
            if s[i] == '(':
                # Push index of opening bracket
                stack.append(i)
            else:
                # Pop the last opening bracket's index
                stack.pop()
                
                if not stack:
                    # Stack is empty, push current index as new reference
                    stack.append(i)
                else:
                    # Calculate length of valid substring
                    current_length = i - stack[-1]
                    max_length = max(max_length, current_length)
        
        return max_length