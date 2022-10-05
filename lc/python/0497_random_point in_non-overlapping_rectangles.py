# binary search and random

# solution is from https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/discuss/805232/Python-Short-solution-with-binary-search-explained

Basically, this problem is extention of problem 528. Random Pick with Weight, let me explain why. Here we have several rectangles and we need to choose point from these rectangles. We can do in in two steps:

Choose rectangle. Note, that the bigger number of points in these rectangle the more should be our changes. Imagine, we have two rectangles with 10 and 6 points. Then we need to choose first rectangle with probability 10/16 and second with probability 6/16.
Choose point inside this rectangle. We need to choose coordinate x and coordinate y uniformly.
When we initailze we count weights as (x2-x1+1)*(y2-y1+1) because we also need to use boundary. Then we evaluate cumulative sums and normalize.

For pick function, we use binary search to find the right place, using uniform distribution from [0,1] and then we use uniform discrete distribution to choose coordinates x and y.

Complexity: Time and space complexity of __init__ is O(n), where n is number of rectangles. Time complexity of pick is O(log n), because we use binary search. Space complexity of pick is O(1).

Remark: Note, that there is solution with O(1) time/space complexity for pick, using smart mathematical trick, see my solution of problem 528: https://leetcode.com/problems/random-pick-with-weight/discuss/671439/Python-Smart-O(1)-solution-with-detailed-explanation

class Solution:

    def __init__(self, rects: List[List[int]]):
        w = [(x2-x1+1)*(y2-y1+1) for x1,y1,x2,y2 in rects]
        print(f"rects {rects}, w {w}")
        self.weights = [i/sum(w) for i in accumulate(w)]
        print(f"weights {self.weights}")
        self.rects = rects

    def pick(self) -> List[int]:
        n_rect = bisect.bisect(self.weights, random.random())
        x1, y1, x2, y2 = self.rects[n_rect] 
        return [random.randint(x1, x2),random.randint(y1, y2)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
