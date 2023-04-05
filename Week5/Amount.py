
def amount(A, S):
    A.sort()
    result = []
    
    def amountHelper(point, S, rst):
        if S == 0:
            result.append(rst[::])
            return
        if point == len(A) or S < 0:
            return
        prev = None
        for i in range(point, len(A)):
            cur = A[i]
            if cur == prev:
                continue    
            rst.append(cur)
            amountHelper(i+1, S - cur, rst)
            rst.pop()
            prev = cur
        
    amountHelper(0, S, [])
    
    return result
        
if __name__ == "__main__":
    print(amount([11,1,3,2,6,1,5], 8))


from copy import deepcopy

def combination_sum_helper(nums, start, result, remainder, combination):

    if(remainder == 0):
        result.append(deepcopy(combination))
        return
    elif( remainder <0):
        return # sum exceeded the target
    for i in range(start, len(nums)):
        combination.append(nums[i])
        combination_sum_helper(nums, i, result, remainder-nums[i], combination)
        #backtrack
        combination.pop()


def combination_sum(nums, target):
    result = []
    combination_sum_helper(nums,0, result, target,[])
    print(result)

print(combination_sum([2,3,6,7], 7 ))