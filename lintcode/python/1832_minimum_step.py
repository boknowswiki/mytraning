#!/usr/bin/python -t

# bfs

# 解题思路
# 可以将棋盘看作一个所有边权为 11 的图，棋盘的格子就是图的节点，每个节点与相邻的节点各有一条边，与相同颜色的格子有一条边。我们需要在图上找到一条从位置 00 到位置 n - 1n−1 的最短路。
# 
# 由于图的边权均为 11，我们可以通过宽度优先搜索来完成。宽度优先搜索通过维护一个队列来计算最短路，每次取出队首的元素，并将相邻的未访问过的点加入队列，更新他们的最短距离。由于边权为 11 的性质，可以保证队列中存放的节点的距离的差的绝对值小于等于 11，同时也保证了队列中的单调性，从而证明了计算最短路的正确性。
# 
# 如果把同颜色间的节点两两连边建图的话，空间开销会达到 O(N^2)O(N 
# 2
#  )，内存限制不允许这么做。可以单独把每个颜色的节点分组记录下来，每次取出节点后，优先将相同颜色的节点加入队列，这样不会访问到多余的边，且空间开销也会降低到 O(N)O(N)。
# 
# 代码思路
# 将节点按颜色分组到二维数组 colorGroupcolorGroup中。
# 新建一个队列，将节点 00 加入到队列中，且更新节点 00 的状态。
# 取出队首节点 pospos，代表当前搜索的位置。
# 将未访问过的同颜色节点加入队列，并更新状态。
# 将左右两个位置未访问过的节点加入队列，并更新状态。
# 如果队列中还有元素，回到第 33 步，直到队列是空的为止。
# 返回节点 n-1n−1 的最短路。
# 复杂度分析
# 设棋盘的长度为 NN。
# 
# 时间复杂度
# 棋盘上每个节点最多被访问 11 次，时间复杂度为 O(N)O(N)。
# 空间复杂度
# 做宽度优先搜索的队列最多有 NN 个元素，空间开销为 O(N)O(N)。
# 记录最小步数，被访问过颜色和格子，以及颜色分类，空间开销为 O(N)O(N)。
# 综上，总空间复杂度为 O(N)O(N)。

class Solution:
    """
    @param colors: the colors of grids
    @return: return the minimum step from position 0 to position n - 1
    """
    def minimumStep(self, colors):
        # write your code here
        n = len(colors)
        # 记录最小步数
        min_step = {}
        # 记录被访问过的位置
        visited_grid = set()
        # 记录被访问过的颜色
        visited_color = set()
        
        # 按颜色分类
        color_group = [[] for _ in range(n + 1)]
        for i in range(n):
            color_group[colors[i]].append(i)
        
        que = collections.deque()
        que.append(0)
        min_step[0] = 0
        visited_grid.add(0)
        
        while que:
            pos = que.popleft()
            color = colors[pos]
            # 如果某个颜色未处理过，先处理这个颜色
            if color not in visited_color:
                visited_color.add(color)
                for newPos in color_group[color]:
                    if self.isValid(n, newPos, visited_grid):
                        min_step[newPos] = min_step[pos] + 1
                        que.append(newPos)
                        visited_grid.add(newPos)
            
            # 左移右移情况
            newPos = pos + 1
            if self.isValid(n, newPos, visited_grid):
                min_step[newPos] = min_step[pos] + 1
                que.append(newPos)
                visited_grid.add(newPos)
            newPos = pos - 1
            if self.isValid(n, newPos, visited_grid):
                min_step[newPos] = min_step[pos] + 1
                que.append(newPos)
                visited_grid.add(newPos)
        
        return min_step[n - 1]
    
    def isValid(self, n, position, visited_grid):
        if position < 0 or position >= n:
            return False
        if position in visited_grid:
            return False
        return True
