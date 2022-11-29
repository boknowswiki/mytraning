# hash map
# time O(1)
# space O(n)

import random

class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.pos = {}
        

    def insert(self, val: int) -> bool:
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums)-1
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.pos:
            last = self.nums[-1]
            self.nums[self.pos[val]], self.nums[-1] = last, val
            self.pos[val], self.pos[last] = len(self.nums)-1, self.pos[val]
            self.nums.pop()
            del self.pos[val]
            return True
        return False
        

    def getRandom(self) -> int:
        #print(f"nums {self.nums}, pos {self.pos}")
        return self.nums[random.randint(0, len(self.nums) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
