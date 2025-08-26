class Solution:
    def reorganizeString(self, s : str) -> str:
        counts = Counter(s)
        prev = None
        res = ""

        maxHeap = [[-cnt, char] for char, cnt in counts.items()]
        heapq.heapify(maxHeap)

        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            

            cnt, char = heapq.heappop(maxHeap)

            cnt += 1
            res += char

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            if cnt != 0:
                prev = [cnt, char]
            
        return res

        
            
