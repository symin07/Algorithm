
'''
recursive solution Time complexity - O(2^n)
source: https://www.educative.io/courses/dynamic-programming-in-python/xoG0Lmq84yn
'''

def rodCutting_naive(n, prices):
  if n<0:
    return 0
  max_val = 0
  for i in range(1,n+1):
      max_val = max(max_val, prices[i-1] + rodCutting_naive(n - i, prices))
  return max_val

'''
source: https://www.educative.io/courses/dynamic-programming-in-python/xoG0Lmq84yn
'''
def rodCutting_topdown_helper(n, prices, memo):
  if n<0:
    return 0
  if n in memo:
    return memo[n]
  max_val = 0
  for i in range(1,n+1):
      max_val = max(max_val, prices[i-1] + rodCutting_topdown_helper(n - i, prices, memo))
  memo[n] = max_val
  return memo[n]

def rodCutting_topdown(n, prices):
  memo = {}
  return rodCutting_topdown_helper(n, prices, memo)


  '''
 time complexity would be O(n^2).
'''
def rodCutting_bottomup(n, prices):
  # Create a dp array the size of (n+1)
  #dp[1] = best price for length 1 and so on...
  dp = [0 for _ in range(n + 1)]

  # starting from rod of length 1, find optimal answer to all subproblems
  for length in range(1, n + 1):
    max_val = 0
    # for a rod of length i, we can find what cuts give max answer since we have answer to all smaller cuts
    for possible_cut in range(length):
        #If we find a better price replace max value and solution array sol[i] to point to the length that gave us max value
        #since the index of possible cut starts with 0, to get its value we need to do +1 when accessing dp table
        if((prices[possible_cut] + dp[length-(possible_cut+1)]) > max_val):
            max_val = prices[possible_cut] + dp[length-(possible_cut+1)]

    dp[length] = max_val
  # return answer to n length rod
  return dp[n]