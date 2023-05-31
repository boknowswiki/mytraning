# hash table, string

class UndergroundSystem:

    def __init__(self):
        self.id = dict()
        self.stations = dict()
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.id:
            return
        
        self.id[id] = (stationName, t)

        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.id:
            return

        start, start_time = self.id[id]
        if (start, stationName) not in self.stations:
            self.stations[(start, stationName)] = (t-start_time, 1)
        else:
            total, cnt = self.stations[(start, stationName)]
            total += t-start_time
            cnt += 1
            self.stations[(start, stationName)] = (total, cnt)
        del self.id[id]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, cnt = self.stations[(startStation, endStation)]
        return float(total)/float(cnt)
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)


class UndergroundSystem:

    def __init__(self):
        self.check_in_data = {}
        self.journey_data = collections.defaultdict(lambda : [0, 0])
                
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in_data[id] = [stationName, t]

    def checkOut(self, id: int, end_station: str, t: int) -> None:
        # Access and remove the data for id. Note that removing it is actually
        # optional, but we'll discuss the benefits of it in the space complexity
        # analysis section.
        start_station, start_time = self.check_in_data.pop(id)
        self.journey_data[(start_station, end_station)][0] += (t - start_time)
        self.journey_data[(start_station, end_station)][1] += 1
            
    def getAverageTime(self, start_station: str, end_station: str) -> float:
        total_time, total_trips = self.journey_data[(start_station, end_station)]
        # The average is simply the total divided by the number of trips.
        return total_time / total_trips
