class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        #digits = "0123456789"

        res = 0

        for i in operations:
            if i == '+':
                stack.append(stack[-1] + stack[-2])
            elif i == 'D':
                stack.append(stack[-1] * 2)
            elif i == 'C':
                stack.pop()
            else:
                stack.append(int(i))
            
        print(stack)
        res = sum(stack)
        return res
            
