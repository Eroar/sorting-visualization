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
        colWidth = math.floor(self._res[0]/len(listOfColumns))

        highestCol = max(listOfColumns)
        self._screen.fill(self._background)
        for columnH, columnColor, i in zip(listOfColumns, listOfColors, range(len(listOfColumns))):
            high2Draw = self._res[1] - math.floor(self._res[1] * (columnH/highestCol))
            pygame.draw.rect(self._screen, columnColor, (i*colWidth, high2Draw, colWidth, self._res[1]-high2Draw), 0)
        
        diffs = self._getDifferenceInLists(self._lastListOfColors, listOfColors)
        diffs2 = self._getDifferenceInLists(self._lastListOfColumns, listOfColumns)
        if diffs2!=-1:
            diffs += diffs2
        print("diffs", diffs)
        if diffs== -1:
            pygame.display.update()
        else:
            rects=[]
            for diff in diffs:
                rects.append(pygame.Rect(diff*colWidth, 0, colWidth, self._res[1]))
            pygame.display.update(rects)
        self._lastListOfColors = listOfColors
        self._lastListOfColumns = listOfColumns


if __name__ == "__main__":
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    screen = Screen()
    while True:
        screen.drawColumns([1,5,3], [red, green, blue])