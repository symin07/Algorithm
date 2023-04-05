fibMemo = {0:1, 1:1}
def Fib_top_down(n):
    print("Calculate for n: %s, FibMemo = %s" % (n, fibMemo))
    if n in fibMemo:
        print("found for n: %s, FibMemo = %s" % (n, fibMemo))
        return fibMemo[n]
    fibMemo[n] = Fib_top_down(n-1) + Fib_top_down(n-2)
    print("Returning Answer for n: %s" % (n))
    return fibMemo[n]

print(Fib_top_down(5))
print(Fib_top_down(7))
print(Fib_top_down(5))