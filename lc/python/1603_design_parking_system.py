# hash table

import collections

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.avail = collections.defaultdict(int)
        self.avail[1] = big
        self.avail[2] = medium
        self.avail[3] = small
        self.parking = collections.defaultdict(int)
        

    def addCar(self, carType: int) -> bool:
        if self.parking[carType] < self.avail[carType]:
            self.parking[carType] += 1
            return True
        else:
            return False

        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):

        # Number of empty slots for each type of car
        self.empty = [big, medium, small]

    def addCar(self, carType: int) -> bool:

        # If space is available, allocate and return True
        if self.empty[carType - 1] > 0:
            self.empty[carType - 1] -= 1
            return True

        # Else, return False
        return False
