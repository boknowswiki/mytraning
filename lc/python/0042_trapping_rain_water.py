
# two pointers
# time O(n)
# space O(1)

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        l_max = r_max = 0

        ret = 0
        while l < r:
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])
            if height[l] > height[r]:
                diff = min(l_max, r_max) - height[r]
                if diff > 0:
                    ret += diff
                r -= 1
            else:
                diff = min(l_max, r_max) - height[l]
                if diff > 0:
                    ret += diff
                l += 1

        return ret

class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        ret = l_max = r_max = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] > l_max:
                    l_max = height[l]
                else:
                    ret += l_max - height[l]
                l += 1
            else:
                if height[r] > r_max:
                    r_max = height[r]
                else:
                    ret += r_max - height[r]

                r -= 1

        return ret

# stack
# time O(n)
# space O(n)

class Solution:
    def trap(self, height: List[int]) -> int:
        st = []
        cur = 0
        ret = 0

        while cur < len(height):
            while st and height[cur] > height[st[-1]]:
                top = st.pop()
                if not st:
                    break
                dist = cur - st[-1]-1
                h = min(height[cur], height[st[-1]]) - height[top]
                ret += dist * h

            st.append(cur)
            cur += 1
        
        return ret
      
 
