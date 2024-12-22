class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        

        res = defaultdict(list)
        for string in strs:
            sorted_string = ''.join(sorted(string))
            res[sorted_string].append(string)
        
        anagrams = list(res.values())
        return anagrams
            
            
            
            