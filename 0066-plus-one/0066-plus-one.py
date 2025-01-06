class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_digits = [str(i) for i in digits]
        res = str(int((''.join(str_digits))) + 1)
        converted = [int(i) for i in res]
        return converted
