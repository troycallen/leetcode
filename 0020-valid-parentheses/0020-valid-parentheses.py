class Solution:
    def isValid(self, s: str) -> bool:
        valid_map = { 
            "}": "{",
            ")": "(",
            "]": "["
        }

        stack = []

        for i in s:
            if i in valid_map:
                if stack[-1] == valid_map[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        return len(stack) == 0

        
