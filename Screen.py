import pygame
import math

pygame.init()

class Screen:
    def __init__(self, res=(640, 480), background=(0, 0, 0)):
        self._screen = pygame.display.set_mode(res)
        self._res = res
        self._background = background
        self._lastListOfColors = []
        self._lastListOfColumns = []

    def _getDifferenceInLists(self, listA, listB):
        if len(listA)!=len(listB):
            return -1
        diff = []
        for a, b, i in zip(listA, listB, range(len(listA))):
            if a!=b:
                diff.append(i)
        return diff
    
    def drawColumns(self, listOfColumns, listOfColors):
        if len(listOfColumns)!=len(listOfColors):
            raise Exception("len(listOfColumns)!=len(listOfColors)")
        colWidth = self._res[0]/len(listOfColumns)

        highestCol = max(listOfColumns)
        self._screen.fill(self._background)
        for columnH, columnColor, i in zip(listOfColumns, listOfColors, range(len(listOfColumns))):
            high2Draw = self._res[1] - self._res[1] * (columnH/highestCol)
            pygame.draw.rect(self._screen, columnColor, (i*colWidth, high2Draw, colWidth, self._res[1]-high2Draw), 0)
        
        diffs = self._getDifferenceInLists(self._lastListOfColumns, listOfColumns)
        diffs2 = self._getDifferenceInLists(self._lastListOfColors, listOfColors)
        
        if (diffs == -1) and (diffs2 == -1):
            pygame.display.update()
        
        else:
            if diffs == -1:
                diffs = []
            if diffs2!=-1:
                diffs += diffs2
            rects=[]
            for diff in diffs:
                rects.append(pygame.Rect(diff*colWidth, 0, colWidth, self._res[1]))
            pygame.display.update(rects)
        self._lastListOfColors = listOfColors.copy()
        self._lastListOfColumns = listOfColumns.copy()


if __name__ == "__main__":
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    screen = Screen()
    while True:
        screen.drawColumns([1,5,3], [red, green, blue])
        for event in pygame.event.get():
            # Close the program if the user presses the 'X'
            if event.type == pygame.QUIT:
                quit()