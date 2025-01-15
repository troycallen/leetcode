class Leaderboard:

    def __init__(self):
        self.player_scores = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.player_scores:
            self.player_scores[playerId] += score
        else:
            self.player_scores[playerId] = score

    def top(self, K: int) -> int:
        min_heap = []
        for i in self.player_scores.values():
            if len(min_heap) < K:
                heapq.heappush(min_heap, i)
            else:
                heapq.heappushpop(min_heap, i)
        
        return sum(min_heap)

    def reset(self, playerId: int) -> None:
        self.player_scores[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)