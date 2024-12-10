class UndergroundSystem:

    def __init__(self):
        self.checkinMap = {}    # id - station, time
        self.totalMap = {}      # start, end - time, number of ppl down the route
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkinMap[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, time = self.checkinMap[id]
        end = stationName
        if (start,end) not in self.totalMap:
            self.totalMap[(start,end)]= [0,0]
        self.totalMap[(start,end)][0] += t - time
        self.totalMap[(start,end)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time, checkins = self.totalMap[(startStation, endStation)]
        #print(time, checkins)
        res = time/checkins
        return res
    
    
  


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)