class Leaderboard:

    def __init__(self):
        self.leaderboard = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.leaderboard:
            self.leaderboard[playerId] += score
        else:
            self.leaderboard[playerId] = score

    def top(self, K: int) -> int:
        return sum(sorted(self.leaderboard.values(), reverse = True)[:K])
        

    def reset(self, playerId: int) -> None:
        self.leaderboard[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)