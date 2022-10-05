# stack
# time O(n)
# space O(n)

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        st = []
        second_num = -sys.maxsize-1
        
        for num in nums[::-1]:
            #print(f"st {st}, second {second_num}, num {num}")
            if num < second_num:
                return True
            while st and st[-1] < num:
                second_num = st.pop()
                
            st.append(num)
            
        return False
