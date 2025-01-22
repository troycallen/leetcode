class UndergroundSystem:

    def __init__(self):
        self.checkins = {}      # id -> station, time
        self.travelTimes = {}   # start,end -> time, count

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = stationName, t

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, time = self.checkins[id]
        total_time = t - time
        end = stationName

        if (start,end) in self.travelTimes:
            self.travelTimes[(start,end)][0] += total_time
            self.travelTimes[(start,end)][1] += 1
        else:
            self.travelTimes[(start,end)] = [total_time, 1]
        
        del self.checkins[id]
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time, count = self.travelTimes[(startStation, endStation)]

        return time/count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)