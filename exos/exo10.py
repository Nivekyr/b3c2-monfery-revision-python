def insertionSort(slist):
    for i in range(1, len(slist)):
 
        key = slist[i]
        j = i-1
        while j >= 0 and key < slist[j] :
                slist[j + 1] = slist[j]
                j -= 1
        slist[j + 1] = key

    return slist

slist = [15, 3, 8, 10, 19, 2, 7, 14, 1, 20, 12, 6, 18, 4, 11, 9, 17, 5, 13, 16]
print(insertionSort(slist))
