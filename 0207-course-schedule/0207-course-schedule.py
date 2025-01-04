class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i : [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            pre_map[course].append(prereq)
        

        visited = set()

        def dfs(i):
            # we have a cycle
            if i in visited:
                return False
            
            # course has no pre reqs
            if pre_map[i] == []:
                return True

            
            visited.add(i)
            for pre in pre_map[i]:
                if not dfs(pre):
                    return False
            visited.remove(i)

            pre_map[i] = True
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True

        
