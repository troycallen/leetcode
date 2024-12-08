class UndergroundSystem:

    def __init__(self):
        self.checkinMap = {} # id -> start station, time
        self.totalMap = {} # start startion, end station -> [total time, count of people down the route]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkinMap[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, time = self.checkinMap[id]
        if (start, stationName) not in self.totalMap:
            self.totalMap[(start, stationName)] = [0, 0]
        self.totalMap[(start, stationName)][1] += 1
        self.totalMap[(start, stationName)][0] += t - time

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.totalMap[(startStation, endStation)]
        return total/count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)