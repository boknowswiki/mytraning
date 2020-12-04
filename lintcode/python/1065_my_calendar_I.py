#!/usr/bin/python -t

# 1.这是一道设计型题目，与常见的完整一个方法的题目不同，要求实现MyCalendar类的构造函数和book函数。
# 2. 方法一（直接遍历）：
# 1. 最容易想到的方法是，用一个list或者vector之类的数据结构，记录所有已经添加的时间段。每添加一个新的时间段，就遍历这个列表，看是否存在重叠。如果没有重叠，则把新的时间段也加入列表。
# 2. 两个时间段[s1, e1)和[s2, e2)不重叠，当且仅当e1 <= s2 或 e2 <= s1.
# 3. 复杂度分析：
# 1. 时间复杂度：O(N ^ 2)，N是添加成功的时间段数量。因为每添加一个时间段，要遍历的list长度分别为0，1，....，N - 1，求和得到(N - 1) * N / 2，也即O(N ^ 2)。
# 2. 空间复杂度：O(N)， 用于记录所有添加成功的时间段。
# 3. 方法二：（构造特殊的二叉搜索树 (https://baike.baidu.com/item/%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91/7077855?fr=aladdin)）
# 1. 类似在常见的二叉搜索树中查找某个数一样，如果我们能够实现出一种特殊的二叉搜索树，使得：
# 1. 树中每个节点是已加的一个时间段。
# 2. 能方便地查找新时间段与树中节点是否重叠。
# 2. 这样就能大幅提高效率。庆幸的是，这种想法是可行的。
# 3. 具体地，从树根开始搜索，当前搜索节点指向树根。新的时间段与当前节点有三种可能：
# 1. 完全在当前节点左侧，则当前节点指向左孩子；
# 2. 完全在当前节点右侧，则当前节点指向右孩子；
# 3. 有重叠，直接返回false。
# 4. 循环该过程，直到当前节点指空。指空说明新的时间段与整棵树无重叠，则把新的时间段添加在当前位置，并返回true。
# 5. 至此，整个算法已经结束。下文给出两点补充：
# 1. 有的同学可能会问，为什么这种做法是正确的？为什么当前节点指空一定说明无重叠？要注意，二叉搜索树的作用可看作是提供了一个排好序的列表，在二叉搜索树中搜索就像是在这个有序列表搜索某个元素一样，如果当前节点指空，说明指向了有序列表的两个相邻元素中间位置，这也就意味着搜索不到该元素。在这里，即是新时间段与所有时间段无重叠。
# 2. 如果使用的是Java，那么可以使用TreeMap (https://docs.oracle.com/javase/7/docs/api/java/util/TreeMap.html)这种数据结构。TreeMap 是一个有序的key-value集合，它通过红黑树 (http://www.cnblogs.com/skywang12345/p/3245399.html)实现，继承于AbstractMap，所以它是一个Map，即一个key-value集合。TreeMap可以查询小于等于某个值的最大的key，也可查询大于等于某个值的最小的key。所以，在该题中，对于每个以start开始、end结束的新时间段，若用start做key，end做value，只需查询TreeMap中start值相邻两侧的key，保证左侧end <= start <= end <= 右侧start即可。这种方法与前述方法二类似，都是使用了二叉搜索树（TreeMap所使用的红黑树也是一种二叉搜索树），只不过这里的节点有一种以start做key，end做value的特殊结构，但原理相同，所以仍可看作是方法二。
# 6. 复杂度分析：
# 1. 时间复杂度：O(N * logN)，N是添加成功的时间段数量，对于每一个时间段的搜索需要O(logN)，添加需要O(1)。（*注意：*这里的O(N * logN)只能看作是平均时间复杂度，因为搜索最坏需要O(N)。 如果在手动构造二叉搜索树时实现了平衡处理或者使用了TreeMap等标准库，可保证O(N * logN)仍为最坏时间复杂度）
# 2. 空间复杂度O(N)，用于构造二叉树。


class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left, self.right = None, None
        
        return
    
    def insert(self, start, end):
        if start >= self.end:
            if not self.right:
                self.right = Node(start, end)
                return True
                
            return self.right.insert(start, end)
        elif end <= self.start:
            if not self.left:
                self.left = Node(start, end)
                return True
                
            return self.left.insert(start, end)
            
        else:
            return False
            
        

class MyCalendar(object):

    def __init__(self):
        self.root = None
        
        return
        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        
        if not self.root:
            self.root = Node(start, end)
            return True
            
        return self.root.insert(start, end)
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

