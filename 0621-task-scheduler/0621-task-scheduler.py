class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = [0] * 26

        for task in tasks:
            counts[ord(task) - ord('A')] += 1
    
        counts.sort()
        max_freq = counts[25]
        idle_time = (max_freq - 1) * n

        for i in range(24, -1, -1):
            idle_time -= min(counts[i], max_freq - 1)
        
        min_cycles = len(tasks) + max(0,idle_time)

        return min_cycles

    
    