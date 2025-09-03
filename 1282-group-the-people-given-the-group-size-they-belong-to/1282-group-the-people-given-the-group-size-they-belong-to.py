class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list)
        res = []

        for person, size in enumerate(groupSizes):

            groups[size].append(person)
            if len(groups[size]) == size:
                res.append(groups[size])
                groups[size] = []
        
        return res