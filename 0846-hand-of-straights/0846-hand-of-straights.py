class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        count = dict(sorted(count.items()))

        while count:
            min_elem = next(iter(count))
            for i in range(min_elem, min_elem + groupSize):
                if i not in count:
                    return False
                
                count[i] -= 1
                if count[i] == 0:
                    count.pop(i)
            
        return True
        

        


