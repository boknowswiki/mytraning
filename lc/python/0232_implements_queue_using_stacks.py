# stack
# time O(n)
# space O(n)

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if not len(self.s2):
            while len(self.s1):
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        if not len(self.s2):
            while len(self.s1):
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return (not len(self.s1)) and (not len(self.s2))
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
