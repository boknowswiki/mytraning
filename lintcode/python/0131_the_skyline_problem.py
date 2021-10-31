#!/usr/bin/python -t

# sweep line and sort and heap
# https://briangordon.github.io/2014/08/the-skyline-problem.html

# time O(nlogn) space O(n)

class position:
    def __init__(self, pos, height, flag, id):
        self.pos = pos
        self.height = height
        self.flag = flag
        self.id = id

    def __lt__(self, other):
        return self.pos < other.pos


class my_height:
    def __init__(self, height, id):
        self.height = height
        self.id = id
    def __lt__(self, other):
        return self.height < other.height

class my_heap:
    def __init__(self):
        self.heap = []
        self.map = {}
    def size(self):
        return self.heap.__len__()
    def insert(self, h):
        self.heap.append(h)
        self.map[h.id] = self.size()-1
        cur = self.size()-1
        while cur > 0:
            father = (cur-1)//2
            if self.heap[father] < self.heap[cur]:
                self.swap(father, cur)
            else:
                break
            cur = father
        return

    def max_height(self):
        if self.size() == 0:
            return 0
        return self.heap[0].height

    def delete(self, building_id):
        index = self.map[building_id]
        if index == self.size() - 1:
            self.heap.pop()
            del self.map[building_id]
            return
        self.swap(index, self.size() - 1)
        self.heap.pop()
        
        cur = index
        father = (cur - 1) // 2
        
        if father >= 0 and self.heap[cur] > self.heap[father]:
            while cur > 0:
                father = (cur - 1) // 2
                if self.heap[father] < self.heap[cur]:
                    self.swap(father, cur)
                else:
                    break
                cur = father
        else:
            while cur < self.size():
                left_child, right_child = (cur + 1) * 2 - 1, (cur + 1) * 2 
                if left_child >= self.size():
                    break
                if right_child >= self.size():
                    if self.heap[left_child] > self.heap[cur]:
                        self.swap(left_child, cur)
                    break
                else:
                    if self.heap[left_child] > self.heap[right_child]:
                        max_child = left_child
                    else:
                        max_child = right_child
                    if self.heap[cur] < self.heap[max_child]:
                        self.swap(cur, max_child)
                        cur = max_child
                    else:
                        break
        del self.map[building_id]

    def swap(self, i, j):
        self.map[self.heap[j].id] = i
        self.map[self.heap[i].id] = j
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        return

class Solution:
    """
    @param buildings: A list of lists of integers
    @return: Find the outline of those buildings
    """
    def buildingOutline(self, buildings):
        # write your code here
        positions = []
        id = 0
        for build in buildings:
            positions.append(position(build[0], build[2], 0, id))
            positions.append(position(build[1], build[2], 1, id))
            id += 1
        positions = sorted(positions)
        heapq = my_heap()

        i = 0
        ret = []
        pre_x = -1
        pre_height = 0

        while i < positions.__len__():
            j = i
            while j < positions.__len__() and positions[j].pos == positions[i].pos:
                if positions[j].flag == 0:
                    heapq.insert(my_height(positions[j].height, positions[j].id))
                else:
                    heapq.delete(positions[j].id)
                j += 1

            if heapq.size() == 0:
                ret.append([pre_x, positions[i].pos, pre_height])
                pre_x, pre_height = -1, 0
            else:
                cur_height = heapq.max_height()
                cur_x = positions[i].pos
                if pre_x == -1:
                    pre_x, pre_height = cur_x, cur_height
                elif cur_height != pre_height:
                    ret.append([pre_x, cur_x, pre_height])
                    pre_x, pre_height = cur_x, cur_height
            i = j

        return ret


if __name__ == '__main__':
    s = Solution()
    a = [[1, 3, 3],[2, 4, 4],[5, 6, 1]]
    print(s.buildingOutline(a))