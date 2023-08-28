# queue
# time O(n)
# space O(n)

import collections

class MyStack:

    def __init__(self):
        self.q = collections.deque()
        self.b_q = collections.deque()
        

    def push(self, x: int) -> None:
        self.q.append(x)
        

    def pop(self) -> int:
        for _ in range(len(self.q)-1):
            self.b_q.append(self.q.popleft())

        v = self.q.popleft()
        self.q = self.b_q

        return v
        

    def top(self) -> int:
        if len(self.q) > 0:
            return self.q[len(self.q)-1]

        return -1

    def empty(self) -> bool:
        return len(self.q) == 0

# one queue

    def __init__(self):
        self.q = collections.deque()
        self.last = None

    def push(self, x: int) -> None:
        self.q.append(x)
        self.last = x

    def pop(self) -> int:
        for _ in range(len(self.q) - 1):
            self.last = self.q.popleft()
            self.q.append(self.last)
        if len(self.q) == 1:
            self.last = None
        return self.q.popleft()

    def top(self) -> int:
        return self.last

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
