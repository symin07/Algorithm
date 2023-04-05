'''
Implement a function knapsack_0_1(W, n, weights, values):

Example: knapsack_0_1(10, 5 ,[4, 9, 3, 5, 7], [10, 25, 13, 20, 8] ) should return 33
'''
def knapsack_0_1(W, n, weight, value):
    dp = [[0 for x in range(0, n)] for x in range(W+1)]
    for x in range(1, W+1):
        for i in range(n):
          dp[x][i] = dp[x][i-1]
          if x >= weight[i]:
            dp[x][i] = max(dp[x][i], value[i] + dp[x-weight[i]][i-1])
    return dp[W][n-1]

print(knapsack_0_1(5, 4, [2, 5, 1, 3], [9, 20, 5, 15]))