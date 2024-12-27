class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p, s in zip(position, speed)]
        pair.sort(reverse = True)
        stack = []

        for p,s in pair:
            # appending the time to reach target 
            stack.append((target - p) / s)

            # multiple cars and this one will catch up and form a fleet
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                # so we have to pop a car in order to merge them into fleet
                stack.pop()
            
        num_cars = len(stack)
        return num_cars



        

        