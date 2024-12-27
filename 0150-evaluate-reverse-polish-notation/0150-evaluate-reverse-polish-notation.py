class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack  = []
        res = 0

        for i in tokens:
            if i == '+':
                a,b = stack.pop(), stack.pop()
                stack.append(a + b)
            elif i == '-':
                a,b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif i == '*':
                a,b = stack.pop(), stack.pop()
                stack.append(a * b)
            elif i == '/':
                a,b = stack.pop(), stack.pop()
                stack.append(b / a)
            else:
                stack.append(int(i))
        
        return stack[0]
