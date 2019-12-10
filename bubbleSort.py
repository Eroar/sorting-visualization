def beforeIteration(arr, startingPos, workingOnColor, baseColor):
    if startingPos + 1 == len(arr):
        #Starting pos is to big
        return []

    colorArr = []
    for i in range(len(arr)):
        if i==startingPos or i==startingPos+1:
            colorArr.append(workingOnColor)
        else:
            colorArr.append(baseColor)
    
    return arr, colorArr


def afterIteration(arr, startingPos, workingOnColor, baseColor):
    if startingPos + 1 == len(arr):
        #Starting pos is to big
        return []

    swapped = False
    if arr[startingPos]>arr[startingPos+1]:
        swapped = True
        tmp = arr[startingPos]
        arr[startingPos] = arr[startingPos+1]
        arr[startingPos+1] = tmp
    
    colorArr = []
    for i in range(len(arr)):
        if i==startingPos or i==startingPos+1:
            colorArr.append(workingOnColor)
        else:
            colorArr.append(baseColor)
    
    return arr, colorArr, swapped
