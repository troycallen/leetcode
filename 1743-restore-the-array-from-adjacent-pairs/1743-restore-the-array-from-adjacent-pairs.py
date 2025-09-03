class Solution:
    def restoreArray(self, pairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for a,b in pairs:
            graph[a].append(b)
            graph[b].append(a)

        res = []
        
        for node,neighbor in graph.items():
            if len(neighbor) == 1:
                res = [node, neighbor[0]]
        
        print(res)
        while len(res) < len(pairs) + 1:
            last = res[-1]
            second_to_last = res[-2]

            candidates = graph[last]

            next_element = candidates[1] if candidates[1] != second_to_last else candidates[0]

            res.append(next_element)
    
        return res
        

            
        
        

        

                