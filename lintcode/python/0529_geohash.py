#!/usr/bin/python -t

class GeoHash:
    """
    @param: latitude: one of a location coordinate pair 
    @param: longitude: one of a location coordinate pair 
    @param: precision: an integer between 1 to 12
    @return: a base32 string
    """
    def encode(self, latitude, longitude, precision):
        # write your code here
        _base32 = "0123456789bcdefghjkmnpqrstuvwxyz"
        lat_bin = self.get_bin(latitude, -90, 90)
        lng_bin = self.get_bin(longitude, -180, 180)
        
        ret, b = "", ""
        
        for i in xrange(30):
            b += lng_bin[i] + lat_bin[i]
            
        for i in xrange(0, 60, 5):
            ret += _base32[int(b[i:i+5], 2)]
        
        return ret[:precision]
        
        
    def get_bin(self, lat, start, end):
        b = ""
        for i in xrange(30):
            mid = (start+end)/2.0
            if lat > mid:
                start = mid
                b += "1"
            else:
                end = mid
                b += "0"
                
        return b
