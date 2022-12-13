# linked list, hash map

class Node:
    def __init__(self, key=0, val=0, next=None):
        self.key = key
        self.val = val
        self.next = next

class Bucket:
    def __init__(self):
        self.head = Node()
    def insert(self, key, val):
        if not self.exist(key):
            new_node = Node(key=key, val=val, next=self.head.next)
            self.head.next = new_node
        else:
            prev = self.head
            while prev.next:
                if prev.next.key == key:
                    prev.next.val = val
                    return
                else:
                    prev = prev.next

        return
            
    def delete(self, key):
        prev = self.head

        while prev.next:
            if prev.next.key == key:
                prev.next = prev.next.next
                return
            else:
                prev = prev.next

        return

    def exist(self, key):
        prev = self.head

        while prev.next:
            if prev.next.key == key:
                return True
            prev = prev.next

        return False

    def read(self, key):
        prev = self.head

        while prev.next:
            if prev.next.key == key:
                return prev.next.val
            prev = prev.next

        return -1
class MyHashMap:

    def __init__(self):
        self.hash_size = 769
        self.bucket_list = [Bucket() for _ in range(self.hash_size)]

    def hash(self, key):
        return key % self.hash_size

    def put(self, key: int, value: int) -> None:
        self.bucket_list[self.hash(key)].insert(key, value)
        

    def get(self, key: int) -> int:
        return self.bucket_list[self.hash(key)].read(key)
        

    def remove(self, key: int) -> None:
        self.bucket_list[self.hash(key)].delete(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
