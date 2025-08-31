class Solution:
    def restoreArray(self, pairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a,b in pairs:
            graph[a].append(b)
            graph[b].append(a)
        

        res = []

        print(graph)
        for node, neighbors in graph.items():
            if len(neighbors) == 1:
                res = [node, neighbors[0]]
                break

        
        while len(res) < len(pairs) + 1:
            last = res[-1]
            second_last = res[-2]

            candidates = graph[last]

            next_element = candidates[0] if candidates[0] != second_last else candidates[1]

            res.append(next_element)

        return res