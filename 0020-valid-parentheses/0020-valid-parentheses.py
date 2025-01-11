class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {
            '}':'{',
            ')':'(',
            ']':'['
        }
        stack = []
        
        for i in s:
            if i in char_map:
                if stack and stack[-1] == char_map[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        return len(stack) == 0
        
