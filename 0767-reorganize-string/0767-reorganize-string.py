class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        prev = None
        res = ""

        max_heap = [[-cnt, char] for char, cnt in counts.items()]
        heapq.heapify(max_heap)

        while max_heap or prev:
            if prev and not max_heap:
                return ""
            

            cnt, char = heapq.heappop(max_heap)
            cnt += 1
            res += char

            if prev:
                heapq.heappush(max_heap, prev)
                prev = None
            
            if cnt != 0:
                prev = [cnt, char]
        
        return res
