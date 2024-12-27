class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # will be a pair of temp, index

        for i,t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stack_temp, stack_ind = stack.pop()
                res[stack_ind] = i - stack_ind
            
            stack.append((t, i))
        
        return res
        