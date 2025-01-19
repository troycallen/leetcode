class UndergroundSystem:

    def __init__(self):
        self.checkinMap = {}    # id : station, time
        self.totalMap = {}      # start,end - time, count of ppl
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkinMap[id] = stationName, t

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, time = self.checkinMap[id]
        end = stationName

        if (start, end) in self.totalMap:
            self.totalMap[(start,end)][0] += t - time
            self.totalMap[(start,end)][1] += 1
        else:
            self.totalMap[(start,end)] = [t - time, 1]

        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time, count = self.totalMap[(startStation, endStation)]
        return time / count




# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)