class Solution:
    def restoreArray(self, pairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for a,b in pairs:
            graph[a].append(b)
            graph[b].append(a)
        
        res = []

        for node, neighbors in graph.items():
            if len(neighbors) == 1:
                res = [node, neighbors[0]]
        
        while len(res) < len(pairs) + 1:
            last = res[-1]
            prev = res[-2]

            candidates = graph[last]

            next_element = candidates[1] if candidates[1] != prev else candidates[0]
            
            res.append(next_element)
        
        return res


            
        
        

        

                