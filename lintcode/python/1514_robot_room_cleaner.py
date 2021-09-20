#!/usr/bin/python -t

#dfs 

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """
class Solution:
    """
    :type robot: Robot
    :rtype: None
    """
    def cleanRoom(self, robot):
        #write your code here 
        dirs = [(0, 1), (1, 0),(0, -1), (-1, 0)]
        
        def goBack(robot):
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnRight()
            robot.turnRight()

            return
    
        def dfs(pos, robot, direction, visited):
            if pos in visited:
                return
            visited.add(pos)

            robot.clean()
            
            for _ in dirs:
                if robot.move():
                    dfs((pos[0]+dirs[direction][0], pos[1]+dirs[direction][1]), robot, direction, visited)
                    goBack(robot)
                robot.turnRight()
                direction = (direction+1)%len(dirs)

            return

        dfs((0, 0), robot, 0, set())

        return
