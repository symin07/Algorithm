def powerset_helper(pointer, choices_made, input, result):
    if (pointer < 0):
        result.append(choices_made[:])
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


print(powerset([1,2,3,4]))