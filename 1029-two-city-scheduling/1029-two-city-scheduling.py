class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x : x[0] - x[1])
        total = 0
        
        # First half goes to city A (these are the ones where A is cheaper, or least more expensive)
        # Second half goes to city B
        for i in range(len(costs)):
            if i < len(costs) // 2:
                total += costs[i][0]
            else:
                total += costs[i][1]
        
        return total

        


            