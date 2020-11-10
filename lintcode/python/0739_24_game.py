#!/usr/bin/python -t

#dfs
#题解：
#采用dfs即可，枚举任意两个数，即i和j，然后进行运算，每次将当前的num[i]替换成两数运算后的新数字，并将数字规模减一。每次搜索完成后，需要将num[i]和num[j]还原。

class Solution:
    """
    @param nums: 4 cards
    @return: whether they could get the value of 24
    """
    def compute24(self, nums):
        # write your code here
        nums = [float(num) for num in nums]
        ret = self.dfs(nums, 4)
        return ret
        
    def dfs(self, nums, cnt):
        if cnt == 1:
            if abs(nums[0] - 24) <= 1E-6:
                return True
        
        for i in range(cnt):
            for j in range(i+1, cnt):
                a = nums[i]
                b = nums[j]
                nums[j] = nums[cnt-1]
                nums[i] = a+b
                if self.dfs(nums, cnt-1):
                    return True
                
                nums[i] = a-b
                if self.dfs(nums, cnt-1):
                    return True
                    
                nums[i] = b-a
                if self.dfs(nums, cnt-1):
                    return True
                    
                nums[i] = a*b
                if self.dfs(nums, cnt-1):
                    return True
                    
                if a != 0:
                    nums[i] = b/a
                    if self.dfs(nums, cnt-1):
                        return True
                
                if b != 0:
                    nums[i] = a/b
                    if self.dfs(nums, cnt-1):
                        return True
                        
                nums[i] = a
                nums[j] = b
                
        return False
