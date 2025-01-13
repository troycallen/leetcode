# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        # If no ships, return 0
        if bottomLeft.x > topRight.x or bottomLeft.y > topRight.y:
            return 0
        if not sea.hasShips(topRight, bottomLeft):
            return 0
            
        # If we're at a single point and hasShips is true, we found a ship
        if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
            return 1
            
        # Find mid points to split rectangle into four parts
        midX = (topRight.x + bottomLeft.x) // 2
        midY = (topRight.y + bottomLeft.y) // 2
        
        # Split into 4 quadrants and recurse
        return (
            # Top right quadrant
            self.countShips(sea, topRight, Point(midX + 1, midY + 1)) +
            # Top left quadrant 
            self.countShips(sea, Point(midX, topRight.y), Point(bottomLeft.x, midY + 1)) +
            # Bottom right quadrant
            self.countShips(sea, Point(topRight.x, midY), Point(midX + 1, bottomLeft.y)) +
            # Bottom left quadrant
            self.countShips(sea, Point(midX, midY), bottomLeft)
    )