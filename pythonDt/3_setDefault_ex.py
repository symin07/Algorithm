def usual_dict(dictData):
    """use dict[key]"""
    newData = {}
    for k, v in dictData:
        if k in newData:
            newData[k].append(v)
        else:
            newData[k] = [v]
    return newData

def setDefaultDict(dictData):
    """use setDefault() method"""
    newData = {}
    for k, v in dictData:
        newData.setdefault(k, []).append(v)
    return newData

def testSetdef():
    dictData = (("key1", "value1"),
                ("key2", "value2"),
                ("key2", "value3"),
                ("key2", "value4"),
                ("key2", "value5"),
                )
    print(usual_dict(dictData))
    print(setDefaultDict(dictData))

if __name__ == '__main__':
    testSetdef()
    itemDict =  {
        1:  {
                "item": "watch",
                "weight": "1",
                "value": "10"
            },
        2:  {
                "item": "jewel",
                "weight": "2",
                "value": "20"
            },
        3:  {
                "item": "ring",
                "weight": "3",
                "value": "5"
            },
        4:  {
                "item": "grape",
                "weight": "5",
                "value": "20"
            }, 
        5:  {
                "item": "shirts",
                "weight": "4",
                "value": "15"
            },
    }
    print(itemDict.get(1).get("weight"))    
used = [[0 for j in range(4)] for i in range(3)] 
used[2][2] = 5
print(used[2][2], used[1][3])

rangetTest = 10
for i in range(2, 3):
    print("i = ", i)
