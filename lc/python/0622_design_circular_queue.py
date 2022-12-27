# design queue

from threading import Lock

class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * k
        self.cap = k
        self.count = 0
        self.head_index = 0
        self.lock = Lock()
        

    def enQueue(self, value: int) -> bool:
        with self.lock:
            if self.count == self.cap:
                return False
            self.q[(self.head_index+self.count)%self.cap] = value
            self.count += 1
            
        return True
        

    def deQueue(self) -> bool:
        with self.lock:
            if self.count == 0:
                return False

            self.head_index = (self.head_index+1)%self.cap
            self.count -= 1

        return True
        
    def Front(self) -> int:
        if self.count == 0:
            return -1

        return self.q[self.head_index]
        

    def Rear(self) -> int:
        if self.count == 0:
            return -1

        return self.q[(self.head_index+self.count-1)% self.cap]
        

    def isEmpty(self) -> bool:
        return self.count == 0
        

    def isFull(self) -> bool:
        return self.count == self.cap

# another answer:

class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.capacity = k
        self.head = None
        self.tail = None
        self.count = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.count == self.capacity:
            return False
        
        if self.count == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            newNode = Node(value)
            self.tail.next = newNode
            self.tail = newNode
        self.count += 1
        return True


    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.count == 0:
            return False
        self.head = self.head.next
        self.count -= 1
        return True


    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.count == 0:
            return -1
        return self.head.value

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        # empty queue
        if self.count == 0:
            return -1
        return self.tail.value
    
    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.count == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.count == self.capacity

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
