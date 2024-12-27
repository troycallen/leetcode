class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []
        stack = []
        for p,s in zip(position, speed):
            pair.append((p,s))
        
        pair.sort(reverse = True)

        for p,s in pair:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)

        