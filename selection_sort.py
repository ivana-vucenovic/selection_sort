def ascendingSelectionSort(myList):
    for i in range(len(myList) - 1):
        minimum = i
        for j in range( i + 1, len(myList)):
            if(myList[j] < myList[minimum]):
                minimum = j
        if(minimum != i):
            myList[i], myList[minimum] = myList[minimum], myList[i]
    return myList
arr = [9,1,8,2,7,3,6,4,5,6]
ascendingSelectionSort(arr)