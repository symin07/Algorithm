


def mergeSort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        mergeSort(arr, start, mid)
        mergeSort(arr, mid+1, end)
        merge(arr, start, mid, end)

def merge(arr, start, mid, end):
    leftArraySize = (mid-start)+1
    rightArraySize = (end-mid)

    leftArray = [0]*leftArraySize
    rightArray = [0]*rightArraySize
    
    for i in range(0, leftArraySize):
        leftArray[i] = arr[start + i]

    for i in range(0, rightArraySize):
        rightArray[i] = arr[mid+1+i]

     i = 0
    j = 0
    k = start
    while (i < leftArraySize and j <rightArraySize):
        if(leftArray[i] < rightArray[i]):
            arr[k] = leftArray[i]
            i = i + 1
        else:
            arr[k] = rightArray[j]
            j = j + 1
        k = k + 1
    
    while (i < leftArraySize):
        arr[k] = leftArray[i]
        k = k + 1
        i = i + 1
    
    while(j < rightArraySize):
        arr[k] = rightArray[j]
        k = k + 1
        j = j + 1


# Drviver code
def driverCode()
Arr1 = [1,2,3,5,6]
Arr2 = [3,4,5,6,7]
k = 5



if __name__ ==  "__main__":
    driverCode()