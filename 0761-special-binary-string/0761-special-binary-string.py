class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        subs = []  # To hold special substrings
        count = 0  # To track balance between 1's and 0's
        start = 0  # Start index of current special substring

        # Partition the string into special substrings
        for i, char in enumerate(s):
            count += 1 if char == '1' else -1
            if count == 0:
                # Recursively solve inner part and format as '1' + ... + '0'
                subs.append('1' + self.makeLargestSpecial(s[start + 1:i]) + '0')
                start = i + 1

        # Sort substrings in descending lexicographical order, then join
        subs.sort(reverse=True)
        return ''.join(subs)
