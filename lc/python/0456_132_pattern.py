# stack
# time O(n)
# space O(n)

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        st = []
        min_array = [-1] * n
        min_array[0] = nums[0]

        for i in range(1, n):
            min_array[i] = min(min_array[i-1], nums[i])

        for j in range(n-1, -1, -1):
            if nums[j] <= min_array[j]:
                continue

            while st and st[-1] <= min_array[j]:
                st.pop()

            if st and st[-1] < nums[j]:
                return True

            st.append(nums[j])

        return False


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
