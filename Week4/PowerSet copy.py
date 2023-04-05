# def powerset_backtracking(inputset):
#     powerset(inputset, [])

# def powerset(inputset, result):
#     print(inputset)
#     if inputset not in result:
#         result.append(inputset)
#     for i in range(len(inputset)):
#         powerset(inputset[:i+1], result)
        


# powerset_backtracking([1,2,3])

def powerset_helper(pointer, choices_made, input, result):
    if (pointer < 0):
        copyChmd = choices_made[:]
        result.append(copyChmd)
        return result
    
    choices_made.append(input[pointer])
    powerset_helper(pointer - 1, choices_made, input, result)
    #backtracking
    choices_made.remove(choices_made[len(choices_made) - 1])
    powerset_helper(pointer - 1, choices_made, input, result)

def powerset(input):
    result = []
    powerset_helper(len(input) - 1, [], input, result)
    return result


print(powerset([1,2,3]))