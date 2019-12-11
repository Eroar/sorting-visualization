def bubbleSortGen(arr, workingOnColor, baseColor):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
            colorArr = []
            for k in range(n):
                colorArr.append(baseColor)
            
            colorArr[j]= workingOnColor
            colorArr[j+1]= workingOnColor
            
            yield arr.copy(), colorArr.copy()
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
            yield arr.copy(), colorArr.copy()

if __name__ == "__main__":
    import random
    arr = [random.randint(0, 100) for _ in range(10)]
    print(arr)
    workingOnColor = (255, 0, 0)
    baseColor = (0, 0, 255)
    print("sorting")
    for data, colors in bubbleSort(arr, workingOnColor, baseColor):
        # print(data)
        print(colors)