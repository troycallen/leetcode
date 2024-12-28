class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]

        heapq.heapify(max_heap)
        #print(max_heap)
        time = 0
        queue = deque()     # pair of [-cnt, idletime]

        while max_heap or queue:
            time += 1
            
            if max_heap:
                # we add one since we are using negative values to sim a max heap
                # and we want to decrement the count of this letter
                cnt = heapq.heappop(max_heap) + 1
                if cnt:
                    # we append our count and the time that this letter will be available again
                    queue.append([cnt, time + n])
            
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])
            
        return time