# dfs

class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        if not image:
            return 0

        m, n = len(image), len(image[0])
        if image[x][y] != "1":
            return 0

        min_x, max_x, min_y, max_y = x, x, y, y
        v = set()

        def dfs(a, b):
            #print(f"a {a}, b {b}")
            nonlocal v, min_x, max_x, min_y, max_y

            min_x = min(min_x, a)
            max_x = max(max_x, a)
            min_y = min(min_y, b)
            max_y = max(max_y, b)
            
            #print(f"min_x {min_x}, max_x {max_x}, min_y {min_y}, max_y {max_y}")
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for i in range(len(dirs)):
                dx = a + dirs[i][0]
                dy = b + dirs[i][1]
                if 0 <= dx < m and 0 <= dy < n and image[dx][dy] == "1" and (dx, dy) not in v:
                    v.add((dx, dy))
                    dfs(dx, dy)

        v.add((x, y))
        dfs(x, y)

        ret = (max_x - min_x+1) * (max_y - min_y+1)
        return ret
