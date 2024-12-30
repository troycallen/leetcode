class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}

        for i,c in enumerate(s):
            last_index[c] = i

        res = []
        size = 0
        end = 0

        for i, c in enumerate(s):
            size += 1
            end = max(end, last_index[c])

            if i == end:
                res.append(size)
                size = 0
        
        return res

        
            