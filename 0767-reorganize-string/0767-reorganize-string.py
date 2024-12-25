class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)

        # heapify goes off the first value in a pair or lists so we put count first
        maxHeap = [[-cnt, char] for char,cnt in count.items()]
        heapq.heapify(maxHeap) # O (n)

        prev = None
        res = ""

        # we do it while still items in the heap or our previous might exist
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""

            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            if cnt != 0:
                prev = [cnt, char]
        return res
