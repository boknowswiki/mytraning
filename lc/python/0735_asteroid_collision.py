# stack
# time O(n)
# space O(n)

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        
        for asteroid in asteroids:
            if not stk or asteroid > 0:
                stk.append(asteroid)
            else:
                while stk and stk[-1] > 0 and stk[-1] < abs(asteroid):
                    stk.pop()

                if stk and stk[-1] == abs(asteroid):
                    stk.pop()
                else:
                    if not stk or stk[-1] < 0:
                        stk.append(asteroid)
        
        return stk

# my solution
# failed on case [-2, -1, 1, 2], expected [-2, -1, 1, 2], i think should be []
# explaination: Direction matters: negative means moving left, positive means moving right. If negative is to the left of positive which means left is moving left and right is moving right, they will be further and further from each other and never meet.
# for -2, -1 are moving left, and 1, 2 are moving right, they are moving away from each other.

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #print(f"asteroids {asteroids}")
        n = len(asteroids)
        if n < 2:
            return asteroids

        st = [asteroids[0]]
        exploded = False

        def is_collision(a,b):
            return (a >0 and b < 0) or (a < 0 and b > 0)

        for i in range(1,n):
            #print(f"st {st}, i {i}")
            while st and is_collision(st[-1], asteroids[i]):
                if abs(st[-1]) < abs(asteroids[i]):
                    st.pop()
                elif abs(st[-1]) == abs(asteroids[i]):
                    st.pop()
                    exploded = True
                else:
                    exploded = True
                    break

            if exploded:
                exploded = False
                continue
            st.append(asteroids[i])

        return st
