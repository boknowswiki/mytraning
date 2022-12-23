# linked list
# time O(1)
# space O(n)

class Node:
    def __init__(self, key=0, val=0, next=None):
        self.key = key
        self.val = val
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.key_to_pre_node = {}
        self.head = Node()
        self.tail = self.head
        self.cap = capacity
        
        return

    def get(self, key: int) -> int:
        if key not in self.key_to_pre_node:
            return -1

        self.move_to_tail(self.key_to_pre_node[key])

        return self.key_to_pre_node[key].next.val

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_pre_node:
            self.move_to_tail(self.key_to_pre_node[key])
            self.key_to_pre_node[key].next.val = value
            return
        else:
            self.add_to_tail(Node(key, value))
            if len(self.key_to_pre_node) > self.cap:
                self.remove_front()
        
    def move_to_tail(self, prev):
        node = prev.next

        if node == self.tail:
            return

        prev.next = node.next

        if node.next:
            self.key_to_pre_node[node.next.key] = prev
            node.next = None

        self.add_to_tail(node)

        return

    def remove_front(self):
        remove_node = self.head.next
        del self.key_to_pre_node[remove_node.key]
        self.head.next = remove_node.next
        self.key_to_pre_node[self.head.next.key] = self.head

        return
    
    def add_to_tail(self, node):
        self.tail.next = node
        self.key_to_pre_node[node.key] = self.tail
        self.tail = self.tail.next

        return
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
