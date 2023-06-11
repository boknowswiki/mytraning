# binary search, hash table
# time O(nlogn)
# space O(n)

class SnapshotArray:

    def __init__(self, length: int):
        self.id = 0
        self.records = [[[0, 0]] for _ in range(length)]
        

    def set(self, index: int, val: int) -> None:
        self.records[index].append([self.id, val])
        

    def snap(self) -> int:
        self.id += 1
        return self.id - 1
        

    def get(self, index: int, snap_id: int) -> int:
        snap_id = bisect.bisect_right(self.records[index], [snap_id, 10**9])
        return self.records[index][snap_id-1][1]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
