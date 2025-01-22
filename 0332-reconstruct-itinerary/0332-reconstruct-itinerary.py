from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        # Create a graph using a defaultdict of lists
        graph = defaultdict(list)

        # Populate the graph with sorted destinations
        for src, dst in tickets:
            graph[src].append(dst)
        for src in graph:
            graph[src].sort(reverse=True)

        # Initialize the itinerary
        itinerary = []

        # Define the DFS function for Hierholzer's Algorithm
        def dfs(airport):
            while graph[airport]:
                nextDest = graph[airport].pop()
                dfs(nextDest)
            itinerary.append(airport)

        # Start DFS from JFK
        dfs("JFK")

        # Reverse the itinerary to get the correct order
        return itinerary[::-1]