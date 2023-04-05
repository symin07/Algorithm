strGlobal = ""
def reversing_words_slice(word):
    new_words = []
    words = word.split(" ")
    for word in words[::-1]:
        new_words.append(word)
    return " ".join(new_words)

def str_compression(s):
    count, last = 1, ""
    list_aux = []
    for i, c in enumerate(s):
        if last == c:
            count += 1
        else:
            if i != 0:
                list_aux.append(str(count))
            list_aux.append(c)
            count = 1
            last = c
    list_aux.append(str(count))
    return "".join(list_aux)


if __name__ == "__main__":
    str1 = "it is very interesting for me to learn phython"
    str2 = reversing_words_slice(str1)
    result = []

    result.append(4)

    result[0] = 4

    print(result)
    print(str2)   
    
    result = str_compression("aabcccccaaa")
    print(result)

    print("String Operation Test:")
    # str1 = ""
    str2 = "def"
    strConcat = strGlobal + str2
    print(strConcat)
    strGlobal = strGlobal + str2[0]
    print(strGlobal)


    nums = [-1, -3, -4, 6, 7, 3]
    nums = [number for number in nums if number >= 0]
    print("nums:", nums)

    for i in range(10, 2, -1):
        print("i= ",i)
        if (i == 5):
            i -= i


    myList = [1, 2, 3, 4]
    print("myList before deep copy:", myList)
    newList = myList[:]
    print("newList after deep copy:", newList)
    myList.append(5)
    print("myList after deep copy and append 5:", myList)
    print("newList after deep copy and append 5:", newList)

    
    myList2 = [2,3,4,5]
    print("myList2 before deep copy:", myList2)    
    newList2 = list(myList2)
    print("newList2 before deep copy:", newList2)    
    newList2 = list(myList)
    print("newList2 after append myList:", newList2) 

    for col in range(5):
        print("fifth?")

   
   







# string = "kimminho seoyoon"
# fibo = {1:4, 1:10}
# print("use of ::", string[::-1])
# print("real fibo",fibo[1])

# if 0 in fibo:
#     print("0 in fibo: ",  fibo[1])

# print(len(string))
# print(string[1:])

# print(string[-1])
# print(string[0:0])
# print(string[0:8])


# leftArray = [0] * 3
# rightArray = [0] * 10

# print(leftArray)
# print(rightArray)