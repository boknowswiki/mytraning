#!/usr/bin/python -t

class GeoHash:
    """
    @param: geohash: geohash a base32 string
    @return: latitude and longitude a location coordinate pair
    """
    def decode(self, geohash):
        # write your code here
        _base32 = "0123456789bcdefghjkmnpqrstuvwxyz"
        b = ""
        for c in geohash:
            index = _base32.find(c)
            b += self.i2b(index)

        odd = ''.join([b[i] for i in xrange(0, len(b), 2)])
        even = ''.join([b[i] for i in xrange(1, len(b), 2)])

        location = []
        location.append(self.get_location(-90.0, 90.0, even))
        location.append(self.get_location(-180.0, 180.0, odd))
        return location

    def i2b(self, val):
        print val
        
        b = ""
        for i in xrange(5):
            if val % 2:
                b = '1' + b
            else:
                b = '0' + b
            val /= 2
        print b
        return b

    def get_location(self, start, end, string):
        print string
        for c in string:
            mid = (start + end) / 2.0
            if c == '1':
                start = mid
            else:
                end = mid
        return (start + end) / 2.0
