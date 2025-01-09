class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.numList = []

    def insert(self, val: int) -> bool:
        not_present = val not in self.numMap
        if not_present:
            self.numMap[val] = len(self.numList)
            self.numList.append(val)
        

        return not_present

    def remove(self, val: int) -> bool:
        present = val in self.numMap
        if present:
            index = self.numMap[val]
            last_val = self.numList[-1]
            self.numList[index] = last_val
            self.numList.pop()
            self.numMap[last_val] = index
            del self.numMap[val]
            

        return present

    def getRandom(self) -> int:
        return random.choice(self.numList)
        




# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()