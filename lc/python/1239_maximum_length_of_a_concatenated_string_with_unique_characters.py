# string and dfs
# time O(2^n)
# space O(1)

class Solution:
    def __init__(self):
        self.max_len = 0
        
    def maxLength(self, arr: List[str]) -> int:
        if not arr:
            return 0        
        
        self.dfs(arr, "", 0)
        
        return self.max_len
        
    def dfs(self, arr, curr_subseq, idx):
        # return if duplicate characters
        if len(curr_subseq) != len(set(curr_subseq)):
            return
        
        # update max_len if  curr_subseq is maximal
        self.max_len = max(len(curr_subseq), self.max_len)
        
        # dfs on next subseq(s) starting from curr_subseq
        for i in range(idx, len(arr)):
            self.dfs(arr, curr_subseq+arr[i], i+1)

