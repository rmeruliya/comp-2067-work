import pygame
import math
from queue import PriorityQueue

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("path finding algorithm")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Spot:
    def __init__(self,row,col,width,total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width 
        self.total_rows = total_rows
        
    def get_pos(self):
        return self.row, self.col
    def is_closed(self):
        return self.color == RED
    def is_open(self):
        return self.color == GREEN
    def is_barrier(self):
        return self.color == BLACK
    def is_start(self):
        return self.color == ORANGE
    def is_end(self):
        return self.color == TURQUOISE
    def reset(self):
        self.color == WHITE
    def make_closed(self):
        self.color = RED
    def make_open(self):
        self.color = GREEN
    def make_barrier(self):
        self.color = BLACK
    def make_end(self):
        self.color = TURQUOISE
    def make_path(self):
        self.color = PURPLE 
    def draw(self,win):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.width))    
    
    def update_neighbors(self,grid):
        pass
    def __lt__(self,other):
        return False    
    def h(p1,p2):
        x1, y1 = p1
        x2, y2 = p2
        return abs(x1 - x2) + abs(y1 - y2)
    
    def make_grid(rows,width):
        grid = []
        gap = width // rows
        
        
         slow,fast = 0,1
        while fast in range(len(nums)):
            if nums[slow] == nums[fast]:
                fast += 1
            else:
                nums[slow+1] = nums[fast]
                fast += 1
                slow += 1
        return slow + 1
    
     j = 0 
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j
    
    if digits[-1] < 9:
            digits[-1] += 1
            return digits
        elif len(digits) == 1 and digits[0] == 9:
            return [1,0]
        else:
            digits[-1] = 0
            digits[0:-1] = self.plusOne(digits[0:-1])
            return digits