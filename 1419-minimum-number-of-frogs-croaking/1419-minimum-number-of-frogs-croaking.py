class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        """
The Hash Map Counting with Validation algorithm works by maintaining a hash map (dictionary) 
that counts occurrences of each character in the sequence "croak". As we iterate over the input string, 
we validate the sequence order by ensuring that no character appears before its predecessor has appeared enough times. 
We also track the maximum number of frogs croaking simultaneously based on active 'c' to 'k' progressions. 
If at any point the sequence is invalid, we return -1. If valid, the maximum number of concurrent croaks is the answer.
"""

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        croakOrder = "croak"
        charCount = {ch: 0 for ch in croakOrder}

        activeFrogs = 0
        maxFrogs = 0

        for ch in croakOfFrogs:

            charCount[ch] += 1

            for i in range(1, len(croakOrder)):
                if charCount[croakOrder[i]] > charCount[croakOrder[i - 1]]:
                    return -1

            if ch == 'c':
                activeFrogs += 1
                maxFrogs = max(maxFrogs, activeFrogs)

            if ch == 'k':
                activeFrogs -= 1

        if activeFrogs != 0:
            return -1

        return maxFrogs