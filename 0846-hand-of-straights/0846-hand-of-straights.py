class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        #rderedCount = {k: v for k, v in count.items()}

        orderedCount = (dict(sorted(count.items())))
        while orderedCount:
            
            minElem = next(iter(orderedCount))

            for card in range(minElem, minElem + groupSize):
                if card not in orderedCount:
                    return False
                orderedCount[card] -= 1
                if orderedCount[card] == 0:
                    orderedCount.pop(card)
        return True

