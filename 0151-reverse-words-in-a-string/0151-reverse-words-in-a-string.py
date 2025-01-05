class Solution:
    def reverseWords(self, s: str) -> str:
        split_str = s.split()
        res = []

        print(split_str)
        for i in range(len(split_str)- 1, -1, -1):
            res.append(split_str[i])
        

        
        return " ".join(res)