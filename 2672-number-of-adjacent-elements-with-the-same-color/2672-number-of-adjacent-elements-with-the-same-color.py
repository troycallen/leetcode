class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colors = [0] * n
        res = []

        adjCount = 0

        for index, color in queries:
            if colors[index] != 0:
                if index > 0 and colors[index] == colors[index - 1]:
                    adjCount -= 1
                if index < n - 1 and colors[index] == colors[index + 1]:
                    adjCount -= 1
            
            colors[index] = color

            if colors[index] != 0:
                if index > 0 and colors[index] == colors[index - 1]:
                    adjCount += 1
                if index < n - 1 and colors[index] == colors[index + 1]:
                    adjCount += 1
            
            res.append(adjCount)
        
        return res
                