class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for a,b in prerequisites:
            adj[a].append(b)
        # for course schedule ii
        res = []
        cycle = set()
        seen = set()

        def dfs(cur):
            if cur in cycle:
                return False
            if cur in seen:
                return True

            cycle.add(cur)
            for child in adj[cur]:
                if not dfs(child):
                    return False
            cycle.remove(cur)

            seen.add(cur)

            # for course schedule ii 
            res.append(cur) 
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
                
        return res

        
