# design, hash map

class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.avail = set([i for i in range(maxNumbers)])
        self.took = set()

    def get(self) -> int:
        if len(self.avail) == 0:
            return -1

        val = self.avail.pop()
        self.took.add(val)
        return val

    def check(self, number: int) -> bool:
        return number in self.avail
        

    def release(self, number: int) -> None:
        if number in self.took:
            self.took.remove(number)
            self.avail.add(number)

        return
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)


# other's answer

class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        self.maxnum = maxNumbers
        self.available = collections.deque([i for i in range(maxNumbers)])
        self.used = set()
        
    def get(self):
        if not self.available:
            return -1
        res = self.available.popleft()
        self.used.add(res)
        return res
        
    def check(self, number):
        if number < 0 or number >= self.maxnum:
            return False
        return number not in self.used
        
    def release(self, number):
        if number < 0 or number >= self.maxnum or number not in self.used:
            return
        self.used.remove(number)
        self.available.append(number) 
