# linked list

class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularDeque:

    def __init__(self, k: int):
        self.cap = k
        self.count = 0
        self.head = self.tail = Node()
        self.head.prev = self.tail
        self.tail.next = self.head

    def insertFront(self, value: int) -> bool:
        if self.count == self.cap:
            return False

        new_node = Node(val=value)
        self.count += 1
        new_node.next = self.head.next
        new_node.prev = self.head
        self.head.next = new_node

        return True

    def insertLast(self, value: int) -> bool:
        if self.count == self.cap:
            return False

        new_node = Node(val=value)
        self.count += 1
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.tail.next = self.head
        self.head.next = self.tail
        return True

    def deleteFront(self) -> bool:
        if self.count == 0:
            return False

        self.head.next = self.head.next.next
        self.head.next.next.prev = self.head
        self.count -= 1

        return True
        

    def deleteLast(self) -> bool:
        if self.count == 0:
            return False
        prev = self.tail.prev
        self.tail = prev
        self.tail.next = self.head
        self.head.next = self.tail
        self.count -= 1

        return True

    def getFront(self) -> int:
        if self.count == 0:
            return -1

        return self.head.next.val
        

    def getRear(self) -> int:
        if self.count == 0:
            return -1

        return self.tail.val

    def isEmpty(self) -> bool:
        return self.count == 0
        

    def isFull(self) -> bool:
        return self.count == self.cap
        

class Node:
    def __init__(self, value):
        self.val = value
        self.next = self.pre = None
        
class MyCircularDeque:

    def __init__(self, k):
        self.head = self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = k
        self.curSize = 0

    def add(self, value, preNode):
        new = Node(value)
        new.pre = preNode
        new.next = preNode.next
        new.pre.next = new.next.pre = new
        self.curSize += 1
        
    def remove(self, preNode):
        node = preNode.next
        node.pre.next = node.next
        node.next.pre = node.pre
        self.curSize -= 1
    
    def insertFront(self, value):
        if self.curSize < self.size:
            self.add(value, self.head)
            return True
        return False

    def insertLast(self, value):
        if self.curSize < self.size:
            self.add(value, self.tail.pre)
            return True
        return False

    def deleteFront(self):
        if self.curSize:
            self.remove(self.head)
            return True
        return False

    def deleteLast(self):
        if self.curSize:
            self.remove(self.tail.pre.pre)
            return True
        return False

    def getFront(self):
        if self.curSize:
            return self.head.next.val
        return -1

    def getRear(self):
        if self.curSize:
            return self.tail.pre.val
        return -1

    def isEmpty(self):
        return self.curSize == 0

    def isFull(self):
        return self.curSize == self.size

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
