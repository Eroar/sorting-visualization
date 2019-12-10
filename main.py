from Screen import Screen
import time
import random
import bubbleSort
import pygame



if __name__ == "__main__":
    NUMBER_OF_COLUMNS = 200
    # arr = [random.randint(0, 255) for _ in range(NUMBER_OF_COLUMNS)]
    arr = [i for i in range(1,200)]
    random.shuffle(arr)
    workingOnColor = (255, 0, 0)
    baseColor = (0, 0, 255)
    finishedColor = (0, 255, 0)
    
    TIME_BETWEEN = 0

    screen = Screen(res=(1000, 500))

    swapped = True
    while swapped:
        swapped = False
        for sPos in range(len(arr)-1):
            arrBefore, colorArr = bubbleSort.beforeIteration(arr, sPos, workingOnColor, baseColor)
            if TIME_BETWEEN > 0.01:
                screen.drawColumns(arr, colorArr)
                time.sleep(TIME_BETWEEN)

            arrAfter, colorArr, nSwapped = bubbleSort.afterIteration(arrBefore, sPos, workingOnColor, baseColor)
            if nSwapped:
                swapped = True
            screen.drawColumns(arrAfter, colorArr)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            time.sleep(TIME_BETWEEN)
    greenColor = [finishedColor for _ in range(len(arr))]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
    
        screen.drawColumns(arr, greenColor)
        time.sleep(TIME_BETWEEN)

    
            



