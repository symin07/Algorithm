def climbingStairs(n):
    if n <= 0 : return 0
    if n == 1 : return 1
    if n == 2 : return 2
    return climbingStairs(n-1) + climbingStairs(n-2)


print(climbingStairs(5))
print(climbingStairs(3))