# design, binary search, hashmap
# If MM is the number of set function calls, NN is the number of get function calls, and LL is average length of key and value strings.
# time set O(LM) get O(L*logM)
# space set O(LM) get O(1)

class TimeMap:

    def __init__(self):
        self.key_to_time_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.key_to_time_map:
            self.key_to_time_map[key] = []
        
        self.key_to_time_map[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.key_to_time_map:
            return ""
        
        if timestamp < self.key_to_time_map[key][0][0]:
            return ""
        
        l = 0
        r = len(self.key_to_time_map[key]) -1
        
        while l + 1 < r:
            mid = l + (r-l)//2
            if self.key_to_time_map[key][mid][0] <= timestamp:
                l = mid
            else:
                r = mid
                
        if self.key_to_time_map[key][r][0] <= timestamp:
            return self.key_to_time_map[key][r][1]
        return self.key_to_time_map[key][l][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
