# hash map, backtracking, dfs

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 2:
            return []

        ret = []

        def dfs(start, path):
            nonlocal ret
            if len(path) >= 2 and path not in ret:
                ret.append(list(path))

            if start == n:
                return

            for i in range(start, n):
                if len(path) == 0 or nums[i] >= path[-1]:
                    path.append(nums[i])
                    dfs(i+1, path)
                    path.pop()

            return

        dfs(0, [])

        return ret
      
  # better solution
  class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = set()
        sequence = []

        def backtrack(index):
            # if we have checked all elements
            if index == len(nums):
                if len(sequence) >= 2:
                    result.add(tuple(sequence))
                return
            # if the sequence remains increasing after appending nums[index]
            if not sequence or sequence[-1] <= nums[index]:
                # append nums[index] to the sequence
                sequence.append(nums[index])
                # call recursively
                backtrack(index + 1)
                # delete nums[index] from the end of the sequence
                sequence.pop()
            # call recursively not appending an element
            backtrack(index + 1)
        backtrack(0)
        return result
