class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0 
        people.sort()

        l = 0 
        r = len(people) - 1

        while l <= r:
            remaining = limit - people[r]
            r -= 1
            boats += 1
            if people[l] <= remaining and l <= r:
                l += 1
        return boats