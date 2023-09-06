# stack

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        answer = []
        max_height = -1
        
        for current in reversed(range(n)):
            # If there is no building higher (or equal) than the current one to its right,
            # push it in the answer array.
            if max_height < heights[current]:
                answer.append(current)
            
                # Update max building till now.
                max_height = heights[current]
        
        answer.reverse()
        return answer

# stack, monotonic stack

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        if n == 0:
            return []

        ret = []
        st = [(n-1, heights[n-1])]

        for i in range(n-2, -1, -1):
            if heights[i] > st[-1][1]:
                st.append((i, heights[i]))

        #print(f"st {st}")
        while st:
            ret.append(st.pop()[0])

        return sorted(ret)


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        if n == 0:
            return []

        ret = [n-1]
        
        for i in range(n-2, -1, -1):
            if heights[i] > heights[ret[-1]]:
                ret.append(i)

        return sorted(ret)
