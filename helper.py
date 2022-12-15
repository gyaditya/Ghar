def bubbleSort(anArray, key):
    for i in range(len(anArray)):
        for j in range(i+1, len(anArray)):
            if anArray[i][key] > anArray[j][key]:
                anArray[i], anArray[j] = anArray[j], anArray[i]