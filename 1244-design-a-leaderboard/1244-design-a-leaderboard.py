import heapq

class Leaderboard:
    def __init__(self):
        
        # Initialize a dictionary to keep track of player scores
        self.playerScores = {}

    def addScore(self, playerId: int, score: int) -> None:
        
        # Add the given score to the player's total score
        self.playerScores[playerId] = self.playerScores.get(playerId, 0) + score

    def top(self, K: int) -> int:
        
        # Create a min-heap to keep track of top K scores
        minHeap = []
        
        for score in self.playerScores.values():
            
            if len(minHeap) < K:
                
                heapq.heappush(minHeap, score)
            else:
                
                if score > minHeap[0]:
                    
                    heapq.heappushpop(minHeap, score)
        
        # Sum the top K scores
        return sum(minHeap)

    def reset(self, playerId: int) -> None:
        
        # Reset the player's score to 0
        self.playerScores[playerId] = 0

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)