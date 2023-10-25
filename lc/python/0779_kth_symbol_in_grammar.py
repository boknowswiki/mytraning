# recursion
# time O(n)
# space O(n)

class Solution:
    def recursion(self, n: int, k: int) -> int:
        # First row will only have one symbol '0'.
        if n == 1:
            return 0

        total_elements = 2 ** (n - 1)
        half_elements = total_elements // 2

        # If the target is present in the right half, we switch to the respective left half symbol.
        if k > half_elements:
            return 1 - self.recursion(n, k - half_elements)

        # Otherwise, we switch to the previous row.
        return self.recursion(n - 1, k)

    def kthGrammar(self, n: int, k: int) -> int:
        return self.recursion(n, k)

# binary tree
# time O(n)
# space O(n)

class Solution:
    def depthFirstSearch(self, n: int, k: int, rootVal: int) -> int:
        if n == 1:
            return rootVal

        totalNodes = 2 ** (n - 1)

        # Target node will be present in the right half sub-tree of the current root node.
        if k > (totalNodes / 2):
            nextRootVal = 1 if rootVal == 0 else 0
            return self.depthFirstSearch(n - 1, k - (totalNodes / 2), nextRootVal)
        # Otherwise, the target node is in the left sub-tree of the current root node.
        else:
            nextRootVal = 0 if rootVal == 0 else 1
            return self.depthFirstSearch(n - 1, k, nextRootVal)

    def kthGrammar(self, n: int, k: int) -> int:
        return self.depthFirstSearch(n, k, 0)

# recursion, string 
# time limit exceeded

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        
        q = ["0"]

        while n > 1:
            new_q = []
            for e in q:
                if e == "0":
                    new_q.append("0")
                    new_q.append("1")
                else:
                    new_q.append("1")
                    new_q.append("0")
            q = new_q
            n -= 1

        return int(q[k-1])
