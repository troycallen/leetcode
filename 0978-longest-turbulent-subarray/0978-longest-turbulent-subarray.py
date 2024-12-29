class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l = 0
        r = 1

        res = 1
        prev = ""

        while r < len(arr):
            if arr[r - 1] > arr[r] and prev != ">":
                res = max(res, r - l + 1)
                r += 1
                prev = ">"
            elif arr[r - 1] < arr[r] and prev != "<":
                res = max(res, r - l + 1)
                r += 1
                prev = "<"
            # we saw two of same signs in a row or and equals
            # so we want to set previous to be different
            else:
                # skip equal signs
                r = r + 1 if arr[r] == arr[r - 1] else r
                
                # update l 
                l = r - 1
                prev = ""
            
        return res
        

