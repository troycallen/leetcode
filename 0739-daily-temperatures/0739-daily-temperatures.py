class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]
        days = 0

        for i,v in enumerate(temperatures):        
            while stack and stack[-1][0] < v:
                temp, ind = stack.pop()
                res[ind] = i - ind
            stack.append((v, i))
        
        return res