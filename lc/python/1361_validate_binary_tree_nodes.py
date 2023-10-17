# bfs
# time O(n)
# space O(n)

import collections

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        def get_root():
            children = set(leftChild) | set(rightChild)

            for i in range(n):
                if i not in children:
                    return i

            return -1

        root = get_root()
        if root == -1:
            return False

        q = collections.deque([root])
        v = {root}

        while q:
            node = q.popleft()
            for child in [leftChild[node], rightChild[node]]:
                if child != -1:
                    if child in v:
                        return False

                    q.append(child)
                    v.add(child)

        return len(v) == n
