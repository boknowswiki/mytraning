# hash table
# time O(n)
# space O(n)


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        ans = 0
        
        for num in nums:
            ans += counts[num]
            counts[num] += 1
        
        return ans


# time O(n*l)
# space O(n)

import collections

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        m = collections.defaultdict(list)

        for i, num in enumerate(nums):
            m[num].append(i)

        #print(f"m {m}")

        ret = 0

        for k, v in m.items():
            total = 0
            if len(v) > 1:
                cnt = len(v)
                #total = 0
                while cnt > 1:
                    cnt -= 1
                    total += cnt
                    #print(f"cnt {cnt}, total {total}")
            ret += total

        return ret
        
