class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list)
        result = []
        
        for person, size in enumerate(groupSizes):
            groups[size].append(person)
            
            # When we have enough people for a complete group
            if len(groups[size]) == size:
                result.append(groups[size])
                groups[size] = []  # Start new group
        
        return result