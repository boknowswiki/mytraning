# stack
# time O(1)
# space O(n)

class BrowserHistory:

    def __init__(self, homepage: str):
        self.backhist = [homepage]
        self.forwardhist = []
        #print(f"init: back {self.backhist}, forward {self.forwardhist}")

    def visit(self, url: str) -> None:
        self.backhist.append(url)
        self.forwardhist = []
        #print(f"visit: back {self.backhist}, forward {self.forwardhist}")

    def back(self, steps: int) -> str:
        for _ in range(min(steps, len(self.backhist)-1)):
            #print(f"back 1: back {self.backhist}, forward {self.forwardhist}")
            ret = self.backhist.pop()
            #print(f"back 2: back {self.backhist}, forward {self.forwardhist}")
            self.forwardhist.append(ret)

        #print(f"back: back {self.backhist}, forward {self.forwardhist}")
        return self.backhist[-1]
        

    def forward(self, steps: int) -> str:
        for i in range(min(steps, len(self.forwardhist))):
            ret = self.forwardhist.pop()
            self.backhist.append(ret)

        #print(f"forward: back {self.backhist}, forward {self.forwardhist}")
        return self.backhist[-1]

# linked list

class DLLNode:
    def __init__(self, url: str):
        self.data = url
        self.prev, self.next = None, None

class BrowserHistory:
    def __init__(self, homepage: str):
        # 'homepage' is the first visited URL.
        self.linked_list_head = DLLNode(homepage)
        self.current = self.linked_list_head

    def visit(self, url: str) -> None:
        # Insert new node 'url' in the right of current node.
        new_node = DLLNode(url)
        self.current.next = new_node
        new_node.prev = self.current
        # Make this new node as current node now.
        self.current = new_node

    def back(self, steps: int) -> str:
        # Move 'current' pointer in left direction.
        while steps and self.current.prev:
            self.current = self.current.prev
            steps -= 1
        return self.current.data

    def forward(self, steps: int) -> str:
        # Move 'current' pointer in right direction.
        while steps and self.current.next:
            self.current = self.current.next
            steps -= 1
        return self.current.data

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
