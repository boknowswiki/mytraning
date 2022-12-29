#!/usr/bin/python -t

# hash map

class TwoSum:

    def __init__(self):
        self.d = {}
        

    def add(self, number: int) -> None:
        self.d[number] = self.d.get(number, 0) + 1
        

    def find(self, value: int) -> bool:
        for k in self.d:
            need = value - k
            if need != k:
                if need in self.d:
                    return True
            else:
                if self.d[k] >= 2:
                    return True

        return False
        
# sort

class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.is_sorted = False


    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        # Inserting while maintaining the ascending order.
        # for index, num in enumerate(self.nums):
        #     if number <= num:
        #         self.nums.insert(index, number)
        #         return
        ## larger than any number
        #self.nums.append(number)

        self.nums.append(number)
        self.is_sorted = False
    

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        if not self.is_sorted:
            self.nums.sort()
            self.is_sorted = True

        low, high = 0, len(self.nums)-1
        while low < high:
            currSum = self.nums[low] + self.nums[high]
            if currSum < value:
                low += 1
            elif currSum > value:
                high -= 1
            else: # currSum == value
                return True
        
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)

class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.internal = []
        self.dic = {}

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.internal.append(number)
        if number in self.dic:
            # more than once
            self.dic[number] = True
            return
        # once
        self.dic[number] = False

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for v in self.internal:
            if value - v in self.dic:
                if v << 1 == value and not self.dic[v]:
                    continue
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)
