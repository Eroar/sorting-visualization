from Screen import Screen
import time
import random
import bubbleSort
import pygame



if __name__ == "__main__":
    NUMBER_OF_COLUMNS = 10
    arr = [random.randint(0, 255) for _ in range(NUMBER_OF_COLUMNS)]
    workingOnColor = (255, 0, 0)
    baseColor = (0, 0, 255)
    finishedColor = (0, 255, 0)
    
    TIME_BETWEEN = 3

    screen = Screen(res=(1000, 500))

    swapped = True
    while swapped:
        swapped = False
        for sPos in range(len(arr)-1):
            arr, colorArr = bubbleSort.beforeIteration(arr, sPos, workingOnColor, baseColor)
            if TIME_BETWEEN > 0.01:
                # screen.drawColumns(arr, colorArr)
                time.sleep(TIME_BETWEEN)

            arr, colorArr, nSwapped = bubbleSort.afterIteration(arr, sPos, workingOnColor, baseColor)
            if nSwapped:
                swapped = True
            screen.drawColumns(arr, colorArr)
            time.sleep(TIME_BETWEEN)
            for event in pygame.event.get():
                # Close the program if the user presses the 'X'
                if event.type == pygame.QUIT:
                    quit()
    greenColor = [finishedColor for _ in range(len(arr))]
    while True:
        for event in pygame.event.get():
            # Close the program if the user presses the 'X'
            if event.type == pygame.QUIT:
                quit()
    
        screen.drawColumns(arr, greenColor)
        time.sleep(TIME_BETWEEN)

    
            



