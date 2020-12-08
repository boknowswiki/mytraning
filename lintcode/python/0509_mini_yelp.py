'''
Definition of Location:
class Location:
    # @param {double} latitude, longitude
    # @param {Location}
    @classmethod
    def create(cls, latitude, longitude):
        # This will create a new location object

Definition of Restaurant:
class Restaurant:
    # @param {str} name
    # @param {Location} location
    # @return {Restaurant}
    @classmethod
    def create(cls, name, location):
        # This will create a new restaurant object,
        # and auto fill id

Definition of Helper
class Helper:
    # @param {Location} location1, location2
    @classmethod
    def get_distance(cls, location1, location2):
        # return calculate the distance between two location

Definition of GeoHash
class GeoHash:
    # @param {Location} location
    # @return a string
    @classmethom
    def encode(cls, location):
        # return convert location to a geohash string
    
    # @param {str} hashcode
    # @return {Location}
    @classmethod
    def decode(cls, hashcode):
        # return convert a geohash string to location
'''
from YelpHelper import Location, Restaurant, GeoHash, Helper
import bisect


class MiniYelp:

    def __init__(self):
        # initialize your data structure here.
        self.restaurants = {}
        self.ids = {}
        self.geo_values = []


    # @param {str} name
    # @param {Location} location
    # @return {int} restaurant's id
    def add_restaurant(self, name, location):
        # Write your code here
        restaurant = Restaurant.create(name, location)
        hashcode = "%s.%s" % (GeoHash.encode(location), restaurant.id)
        bisect.insort(self.geo_values, hashcode)
        self.restaurants[hashcode] = restaurant
        self.ids[restaurant.id] = hashcode
        print "add ", restaurant.name, hashcode
        
        return restaurant.id

    # @param {int} restaurant_id
    # @return nothing
    def remove_restaurant(self, restaurant_id):
        # Write your code here
        hashcode = self.ids[restaurant_id]
        index = bisect.bisect_left(self.geo_values, hashcode)
        self.geo_values.pop(index)
        del self.ids[restaurant_id]
        del self.restaurants[hashcode]
        
        return


    # @param {Location} location
    # @param {double} k, distance smaller than k miles
    # @return {str[]} a list of restaurant's name and sort by 
    # distance from near to far.
    def neighbors(self, location, k):
        # Write your code here
        dist = self.get_length(k)
        hashcode = GeoHash.encode(location)[:dist]
        left = bisect.bisect_left(self.geo_values, hashcode)
        # "{" is the next character after "z".
        right = bisect.bisect_right(self.geo_values, hashcode+"{")
        
        ret = []
        print left, right, self.geo_values
        
        for i in range(left, right):
            hashvalue = self.geo_values[i]
            restaurant = self.restaurants[hashvalue]
            d = Helper.get_distance(location, restaurant.location)
            if d <= k:
                ret.append((d, restaurant))
                
        ret = sorted(ret, key=lambda r : r[0])
        
        print "find neighbors ", ret
        return [r[1].name for r in ret]
        
        
    def get_length(self, k):
        dist = [2500, 630, 78, 20, 2.4, 0.61, 0.076, 0.01911, 0.00478, 0.0005971, 0.0001492, 0.0000186]
        for i, d in enumerate(dist):
            if k > d:
                return i
                
        return len(dist)
