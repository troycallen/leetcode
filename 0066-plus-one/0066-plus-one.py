class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_digits = [str(i) for i in digits]
        res = int((''.join(str_digits))) + 1
        str_res = str(res)
        converted = []
        for i in str_res:
            converted.append(int(i))
        return converted
