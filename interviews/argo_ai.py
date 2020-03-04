#!/usr/bin/python -t

# https://en.wikipedia.org/wiki/Minesweeper_(video_game)
# Design and implement a class that represents an instance of the map in minesweeper
# Constructor: height, width, num_of_mines # Creates a map with randomly distributed mines
# has_mine: row coordinate, column coordinate => boolean indicating presence of mine.

import random

class mineMap():
    def __init__(self, height=1, width=1, num_of_mines=0):
        if height <= 0 or width <= 0 or num_of_mines <= 0:
            raise Exception()
        if num_of_mines > height*width:
            raise Exception()
            
        self.height = height
        self.width = width
        self.num_of_mines = num_of_mines
        
        self.mine_set = set()
        
        self.total = height * width
        
        # for this part, I can do from 0 - total, and get index random
        # then swap the num with this random index, with start,
        # then shrink the random range to 1 - total, and get index random again
        for i in range(num_of_mines):
            rand_num = random.randint(0, self.total-1)
            if rand_num not in self.mine_set:
                self.mine_set.add(rand_num)
            else:
                rand_num += 1
                if rand_num >= self.total:
                    rand_num %= self.total
                    
                while rand_num in self.mine_set:
                    rand_num += 1
                    rand_num %= self.total
                        
                self.mine_set.add(rand_num)
                
                        
    def has_mine(self, row, col):
        if (row * self.width + col) in self.mine_set:
            return True
        else:
            return False
            
        
        
            
            
        
