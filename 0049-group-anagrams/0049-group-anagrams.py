class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for i in strs:
            counts = [0] * 26
            print(i)
            for c in i:
                #print(c)
                counts[ord(c) - ord('a')] += 1
            
            #print(counts)
            counts = tuple(counts)
            res[counts].append(i)

            
            #res.append()
        
        return list((res.values()))