class RandomizedSet:

    def __init__(self):
        self.numList = []
        self.numMap = {}

    def insert(self, val: int) -> bool:
        res = val not in self.numMap
        if res:
            self.numMap[val] = len(self.numList)
            self.numList.append(val)
        
        return res

    def remove(self, val: int) -> bool:
        res = val in self.numMap
        if res:
            last_val = self.numList[-1]
            val_index = self.numMap[val]
            self.numList[val_index] = last_val
            self.numList.pop()
            self.numMap[last_val] = val_index
            del self.numMap[val]
        return res

    def getRandom(self) -> int:
        return random.choice(self.numList)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()