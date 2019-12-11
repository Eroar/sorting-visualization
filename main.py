from Screen import Screen
import time
import random
from sortingAlgorithms import bubbleSortGen
import pygame


if __name__ == "__main__":
    NUMBER_OF_COLUMNS = 100
    arr = [random.randint(0, 255) for _ in range(NUMBER_OF_COLUMNS)]
    # arr = [i for i in range(1,200)]
    random.shuffle(arr)
    workingOnColor = (255, 0, 0)
    baseColor = (0, 0, 255)
    finishedColor = (0, 255, 0)
    
    TIME_BETWEEN = 0

    screen = Screen(res=(1000, 500))

    bubSort = bubbleSortGen(arr, workingOnColor, baseColor)
    onlyColor = True
    for data, colors in bubSort:
        if onlyColor:
            onlyColor = False
        else:
            screen.drawColumns(data, colors)
            onlyColor = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        time.sleep(TIME_BETWEEN)


    greenColor = [finishedColor for _ in range(len(arr))]
    screen.drawColumns(arr, greenColor)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
    
        time.sleep(TIME_BETWEEN)

    
            



