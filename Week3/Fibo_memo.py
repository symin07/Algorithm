FibMemo = {0:1, 1:1}
def Fib_top_down(n):    
    if n in FibMemo:        
        return FibMemo[n]
    FibMemo[n] = Fib_top_down(n-1) + Fib_top_down(n-2)   
    return FibMemo[n]

print(Fib_top_down(5))


def fib_top_down2(n, fibmemo=None):
    if fibmemo is None:
        fibmemo = {0:1, 1:1}
    if n not in fibmemo:
        fibmemo[n] = fib_top_down2(n-1, fibmemo) + fib_top_down2(n-2, fibmemo)

    return fibmemo[n]