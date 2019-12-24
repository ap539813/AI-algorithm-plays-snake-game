# try:
#     import pygame
#     import sys
#     import math
#     from tkinter import *
#     from tkinter import ttk
#     from tkinter import messagebox
#     import os
# except:
#     import install_requirements  # install packages
import pygame
import sys
import math
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
def main_func(snake_body, goal):

    class spot:
        def __init__(self, x, y):
            self.i = x
            self.j = y
            self.f = 0
            self.g = 0
            self.h = 0
            self.neighbors = []
            self.previous = None
            self.obs = False
            self.closed = False
            self.value = 1

        def path(self, color, st):
            pygame.draw.rect(screen, color, (self.i * w, self.j * h, w, h), st)
            pygame.display.update()

        def addNeighbors(self, grid):
            i = self.i
            j = self.j
            if i < cols-1 and grid[self.i + 1][j].obs == False:
                self.neighbors.append(grid[self.i + 1][j])
            if i > 0 and grid[self.i - 1][j].obs == False:
                self.neighbors.append(grid[self.i - 1][j])
            if j < row-1 and grid[self.i][j + 1].obs == False:
                self.neighbors.append(grid[self.i][j + 1])
            if j > 0 and grid[self.i][j - 1].obs == False:
                self.neighbors.append(grid[self.i][j - 1])


    cols = 45
    grid = [0 for i in range(cols)]
    row = 45
    openSet = []
    closedSet = []
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    grey = (220, 220, 220)
    w = 900 / cols
    h = 900 / row
    cameFrom = []
    result_path = []
    end_game = False

    # create 2d array
    for i in range(cols):
        grid[i] = [0 for i in range(row)]

    # Create Spots
    for i in range(cols):
        for j in range(row):
            grid[i][j] = spot(i, j)


    # Setting the start and end node
    end = grid[goal[0]][goal[1]]
    start = grid[snake_body[-1][0]][snake_body[-1][1]]

    for i in range(0,row):
        grid[0][i].obs = True
        grid[cols-1][i].obs = True
        grid[i][0].obs = True
        grid[i][row-1].obs = True
    openSet.append(start)
    def mousePress(x):
        g1 = x[0]
        g2 = x[1]
        acess = grid[g1][g2]
        if acess != start and acess != end:
            if acess.obs == False:
                acess.obs = True
    for i in snake_body[:-1]:
        mousePress(i)

    for i in range(cols):
        for j in range(row):
            grid[i][j].addNeighbors(grid)

    def heurisitic(n, e):
        d = math.sqrt((n.i - e.i)**2 + (n.j - e.j)**2)
        return d

    def main():
        if len(openSet) > 0:
            lowestIndex = 0
            for i in range(len(openSet)):
                if openSet[i].f < openSet[lowestIndex].f:
                    lowestIndex = i

            current = openSet[lowestIndex]
            if current == end:
                print('done', current.f)
                temp = current.f
                for i in range(round(current.f)):
                    current.closed = False
                    result_path.append((current.i, current.j))
                    current = current.previous
                return result_path
                pygame.quit()

            openSet.pop(lowestIndex)
            closedSet.append(current)

            neighbors = current.neighbors
            for i in range(len(neighbors)):
                neighbor = neighbors[i]
                if neighbor not in closedSet:
                    tempG = current.g + current.value
                    if neighbor in openSet:
                        if neighbor.g > tempG:
                            neighbor.g = tempG
                    else:
                        neighbor.g = tempG
                        openSet.append(neighbor)

                neighbor.h = heurisitic(neighbor, end)
                neighbor.f = neighbor.g + neighbor.h

                if neighbor.previous == None:
                    neighbor.previous = current
        try:
            current.closed = True
        except:
            end_game = True


    while result_path == [] and not end_game:
        main()
    return result_path, end_game
