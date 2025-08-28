class HitCounter:
    def __init__(self):
        self.queue = deque()
    
    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.queue and  timestamp - self.queue[0] >= 300:
            self.queue.popleft()
    
        hits = len(self.queue)

        return hits

        