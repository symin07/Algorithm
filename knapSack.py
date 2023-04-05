

def unboundedKnapsackTopDown(capa, dp, n, itemDict):
    if capa <= 0:
        return 0
    elif dp[capa - 1] != 0:
        return dp.get(capa)
    else:
        for i in range(len(itemDict)):
            dp[i] = unboundedKnapsackTopDown(capa - 1, dp, n, itemDict) + itemDict.get(i).get("value")
    return dp[i]

    
def unboundedKnapsackBottomup(W, n, itemDict):
    dp = [0] * (W+1)
    for x in range(1, W+1):
        for i in range(n):
            if itemDict.get(i).get("weight") <= x:
                dp[x] = max(dp[x], dp[x-itemDict.get(i).get("weight")] + itemDict.get(i).get("value"))
    return dp[W] 

def ZOKnapsackBottomup(W, itemDict):
    dp = [[0 for j in range(len(itemDict))] for i in range(W+1)]
    n = len(itemDict)
    for x in range(1, W+1):
        for i in range(n):
            dp[x][i] = dp[x][i-1]           # It's very core.. before comparing dp[x][i], at least dp[x][i] have dp[x][i-1]
            if (x >= itemDict.get(i).get("weight")):
                dp[x][i] = max(dp[x][i], itemDict.get(i).get("value") + dp[x-itemDict.get(i).get("weight")][i-1])
    return dp[W][n-1]

def knapsack_0_1(W, n, weight, value):
    dp = [[0 for x in range(0, n)] for x in range(W+1)]
    for x in range(1, W+1):
        for i in range(n):
          dp[x][i] = dp[x][i-1]
          if x >= weight[i]:
            dp[x][i] = max(dp[x][i], value[i] + dp[x-weight[i]][i-1])
    return dp[W][n-1]

# Print weights of items that form the optimal solution
def unbound_knapsackOptimalSolution(W, n, weights, values):
    dp = [0]*(W+1)
    sol = [0]*(W+1)

    for x in range(1,W+1):
        for i in range(n):
            wi = weights[i]
            if wi <= x:
                if((dp[x-wi] + values[i] ) > dp[x]):
                    dp[x]=dp[x-wi] + values[i]
                    sol[x]= wi


    w = W
    solution = []
    while w>0:
        solution.append(sol[w])
        w = w-sol[W]

    return solution


print(unbound_knapsackOptimalSolution(10,5,[4,9,3,5,7], [10,25,13,20,8]))



print(knapsack_0_1(5, 4, [2, 5, 1, 3], [9, 20, 5, 15]))



itemDict =  {
    0:  {
            "item": "watch",
            "weight": 2,
            "value": 9
        },
    1:  {
            "item": "jewel",
            "weight": 5,
            "value": 20
        },
    2:  {
            "item": "ring",
            "weight": 1,
            "value": 5
        },
    3:  {
            "item": "shirts",
            "weight": 3,
            "value": 15
        },
}
capa = 5
dp = [0] * 11 
# unboundedKnapsackTopDown(len(dp), dp, len(itemDict), itemDict)
print("The capcity of unboutdedknapsack 10:",unboundedKnapsackBottomup(capa, len(itemDict), itemDict))

print("The capcity of 01knapsack 10:",ZOKnapsackBottomup(capa, itemDict))
