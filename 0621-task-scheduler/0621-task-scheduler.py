class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for i in tasks:
            count[ord(i) - ord('A')] += 1
        
        count.sort()
        maxf = count[25]
        idle = (maxf - 1) * n


        for i in range(24, -1, -1):
            idle -= min((maxf-1, count[i]))
        

        return max(idle, 0) + len(tasks)

        