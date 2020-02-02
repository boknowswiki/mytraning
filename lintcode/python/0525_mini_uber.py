#!/usr/bin/python -t

# hash table

'''
Definition of Trip:
class Trip:
    self.id; # trip's id, primary key
    self.driver_id, self.rider_id; # foreign key
    self.lat, self.lng; # pick up location
    def __init__(self, rider_id, lat, lng):

Definition of Helper
class Helper:
    @classmethod
    def get_distance(cls, lat1, lng1, lat2, lng2):
        # return calculate the distance between (lat1, lng1) and (lat2, lng2)
'''
from Trip import Trip, Helper


class MiniUber:

    def __init__(self):
        # initialize your data structure here.
        self.driver_id_to_location = {}
        self.driver_id_to_trip = {}


    # @param {int} driver_id an integer
    # @param {double} lat, lng driver's location
    # return {trip} matched trip information if there have matched rider or null
    def report(self, driver_id, lat, lng):
        # Write your code here
        if driver_id in self.driver_id_to_trip:
            ret = self.driver_id_to_trip[driver_id]
            #del self.driver_id_to_trip[driver_id]
            return ret
        else:
            self.driver_id_to_location[driver_id] = (lat, lng)
            return None
            


    # @param rider_id an integer
    # @param lat, lng rider's location
    # return a trip
    def request(self, rider_id, lat, lng):
        # Write your code here
        t = Trip(rider_id, lat, lng)
        min_diff = sys.maxint
        match_driver = []
        for driver in self.driver_id_to_location:
            driver_tuple = self.driver_id_to_location[driver]
            diff = Helper.get_distance(lat, lng, driver_tuple[0], driver_tuple[1])
            if diff < min_diff:
                min_diff = diff
                match_driver = [driver, driver_tuple[0], driver_tuple[1]]
        
        if len(match_driver) != 0:
            del self.driver_id_to_location[match_driver[0]]
            t.driver_id = match_driver[0]
            self.driver_id_to_trip[match_driver[0]] = t
            return t
        else:
            return None
            
