def max_independent_set(nums):
    nums = [number for number in nums if number >= 0]
    maxSet = []
    if not nums:
        return maxSet
    n = len(nums)
    dp = [0 for i in range(len(nums))]
    dp[0] = nums[0]    
    #if n == 1:           
    #   return dp[n-1]     for maxSum
    #    maxSet.append(nums[0])
    #    return maxSet
    if n >= 2:
        dp[1] = max(nums[0], nums[1])       
    for i in range(2, n):
        dp[i] = max(nums[i]+dp[i-2], dp[i-1])
    #return dp[n-1]         for maxSum
    # if n == 1:
    #    maxSet.append(dp[0])
    print("Test", dp[n-1])
    if n == 1:
        maxSet.append(dp[0])
        return maxSet
    if n == 2:
        maxSet.append(max(dp[0], dp[1]))
        return maxSet
    i = len(dp) - 1
    while i >= 0:
        if i == 0 or i == 1:
            maxSet.append(dp[i])
            i = i - 2
        elif dp[i] - dp[i-1] == 0:
            i = i - 1
        else:    
            maxSet.append(dp[i] - dp[i-2])
            i = i - 2

    maxSet.reverse()   
    return maxSet


print(max_independent_set([7, 2, 5, 17, 0]))
print(max_independent_set([-1,-1,0]))
print(max_independent_set([90,0, 0, 0, 0]))
print(max_independent_set([0,90, 0, 0]))
print(max_independent_set([-1,-1,-10,-34]))
print(max_independent_set([0, 0, 7, 2, 5, 0, 0, 8, 6, 2]))
print(max_independent_set([1, 4, 10, 7, 0, 0, 90,0, 91, 0, 15, 0, 4, 0, 15,0,0,0,0]))
print(max_independent_set([0,0,7, 0,6,0, 5,3,6,48, 0,0,37, 0,0, 6, 28, 0,9,3,3,4, 0, 19,0,0,0,0, 75]))
