
# * Author: MIN HO KIM 
# * Email: kimminh@oregonstate.edu
# * Date Created: Jan. 17. 2023
# * Filename: kthElement.py
# *
# * Overview:
# *	This is a program using divide and conquer technique
# *	Given two sorted arrays of size m and n respectively, 
# *	this program find the element that would be at the kth
# *	position in combined sorted array. 
# * the time complexity of this program: O(log N) <Log N of arr1 + Log M of arr2>

def kthElement(Arr1, Arr2, k):
    arr1RightMost = len(Arr1)
    arr2RightMost = len(Arr2)

    arr1Mid = arr1RightMost // 2
    arr2Mid = arr2RightMost // 2
    
    numMerged = (arr1Mid + 1) + (arr2Mid + 1)
    
    #Base Case: if one Array is empty, return k-1 index of the other array  
    if not Arr1:
        return Arr2[k-1]
    if not Arr2:
        return Arr1[k-1]

    #General Case:
    if numMerged <= k:                      # kth element is clearly not in array of which mid is smaller, so we can redfine that array from mid to rightmost
        if Arr1[arr1Mid] < Arr2[arr2Mid]:   # If the index of Arr2 is greater, 
            Arr1 = Arr1[arr1Mid + 1:]       # we redefine arr1 because there is clearly no k in array1 from 0 to arr1Mid 
            k = k - (arr1Mid + 1)
        else:   
            Arr2 = Arr2[arr2Mid + 1:]
            k = k - (arr2Mid + 1)
    else:                                   # numMerged > k, kth element is clearly not in array of which mid is bigger, so we can redefine that array from 0 to mid  
        if Arr1[arr1Mid] < Arr2[arr2Mid]:
            Arr2 = Arr2[:arr2Mid]
        else: 
            Arr1 = Arr1[:arr1Mid]

    return kthElement(Arr1, Arr2, k) 

# Drviver code
def driverCode():

    Arr1 = [1,2,3,5,6]
    Arr2 = [3,4,5,6,7]
    k = 5
    print(kthElement(Arr1, Arr2, k))
    assert(kthElement(Arr1, Arr2, k) == 4)

    Arr1 = [1, 3, 8, 10, 15, 20, 30, 40]
    Arr2 = [2, 4, 5, 7, 9, 17, 18, 32, 33, 44, 50, 56]
    k = 10
    print(kthElement(Arr1, Arr2, k))
    assert(kthElement(Arr1, Arr2, k) == 15)
    
if __name__ ==  "__main__":
    driverCode()