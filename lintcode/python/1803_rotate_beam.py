#!/usr/bin/python -t

# two pointers


class Solution:
    """
    @param points: a array of points
    @param angle: a integer
    @return: return a max points with a angle beam
    """
    def AngleBeam(self, points, angle):
        # write your code here
        res, l, r, n = 0, 0, 0, len(points)
        points_angle = []
        for point in points:
            if point[0] != 0:
                points_angle.append(self.transfor(point[0], point[1]))
            else:
                if point[1] > 0:
                    points_angle.append(90.0)
                elif point[1] < 0:
                    points_angle.append(270.0)

        points_angle.sort()
        #print(points_angle)

        for i in range(n):
            points_angle.append(points_angle[i])
            
        #print(points_angle)
        
        while l < n:
            while r < 2*n and self.calculate_angle(points_angle, l, r, n) <= angle:
                r += 1
            if r - l > res:
                res = r - l
            while l < n and self.calculate_angle(points_angle, l, r, n) > angle:
                l += 1

        return res
        
    def transfor(self, x, y):
        flag = 0
        pi, angle = math.atan(1) * 4, (y * 1.0 / x)
        new_angle = math.atan(angle) / pi * 180

        if x > 0 and y >= 0:
            flag = 1
        elif x > 0 and y < 0:
            flag = 4
        elif x < 0 and y >= 0:
            flag = 2
        elif x < 0 and y < 0:
            flag = 3
            
        if flag == 2 or flag == 3:
            new_angle += 180
        elif flag == 4:
            new_angle += 360 
        return new_angle
        
    def calculate_angle(self, pa, l, r, n):
        if r < n:
            return pa[r] - pa[l]
        else:
            return 360 - pa[l] + pa[r]


