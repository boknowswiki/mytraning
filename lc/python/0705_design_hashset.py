# linked list, hash table
# time insert O(1), delete O(n), contains O(n)
# space O(n)

class MyHashSet:

    def __init__(self):
        self.hash_size = 769
        self.bucket_list = [Bucket() for _ in range(self.hash_size)]
        
    def hash(self, val):
        return val % self.hash_size

    def add(self, key: int) -> None:
        key_hash = self.hash(key)
        self.bucket_list[key_hash].insert(key)
        return

    def remove(self, key: int) -> None:
        key_hash = self.hash(key)
        self.bucket_list[key_hash].delete(key)

    def contains(self, key: int) -> bool:
        key_hash = self.hash(key)
        return self.bucket_list[key_hash].exist(key)
        
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Bucket:
    def __init__(self):
        self.head = Node()
    def insert(self, val):
        if not self.exist(val):
            new_node = Node(val=val, next=self.head.next)
            self.head.next = new_node
        return

    def delete(self, val):
        prev = self.head

        while prev.next:
            if prev.next.val == val:
                prev.next = prev.next.next
                return
            else:
                prev = prev.next

        return

    def exist(self, val):
        prev = self.head

        while prev.next:
            if prev.next.val == val:
                return True
            prev = prev.next

        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
