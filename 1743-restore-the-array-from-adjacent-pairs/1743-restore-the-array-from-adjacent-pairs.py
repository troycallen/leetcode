class Solution:
    def restoreArray(self, pairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a,b in pairs:
            graph[a].append(b)
            graph[b].append(a)
        
        res = []

        for node, neighbor in graph.items():
            if len(neighbor) == 1:
                res = [node, neighbor[0]]
        
        while len(res) < len(pairs) + 1:
            last = res[-1]
            prev = res[-2]

            candidates = graph[last]

            next_ele = candidates[0] if candidates[0] != prev else candidates[1]

            res.append(next_ele)
        
        return res

        

                