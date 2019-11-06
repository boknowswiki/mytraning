#!/usr/bin/python -t

# queue

class AnimalShelter:
    def __init__(self):
        self.cats = []
        self.dogs = []
        self.tot = 0
        
        
    """
    @param: name: a string
    @param: type: an integer, 1 if Animal is dog or 0
    @return: nothing
    """
    def enqueue(self, name, type):
        # write your code here
        self.tot += 1
        if type == 1:
            self.dogs.append((name, self.tot))
        else:
            self.cats.append((name, self.tot))
        
        return

    """
    @return: A string
    """
    def dequeueAny(self):
        # write your code here
        if len(self.dogs) == 0:
            return self.dequeueCat()
        elif len(self.cats) == 0:
            return self.dequeueDog()
        else:
            if self.dogs[0][1] < self.cats[0][1]:
                return self.dequeueDog()
            else:
                return self.dequeueCat()

    """
    @return: A string
    """
    def dequeueDog(self):
        # write your code here
        name = self.dogs[0][0]
        del self.dogs[0]
        return name


    """
    @return: A string
    """
    def dequeueCat(self):
        # write your code here
        name = self.cats[0][0]
        del self.cats[0]
        return name
        
        
