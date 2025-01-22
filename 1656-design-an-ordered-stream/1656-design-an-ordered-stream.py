class OrderedStream:

    def __init__(self, n: int):
        self.stream = {}
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value

        res = []
        if idKey > self.ptr:
            return res
        
        while idKey in self.stream:
            res.append(self.stream[idKey])
            idKey += 1
            self.ptr = idKey

        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)