def BigO(n):
    i = 1
    while i < n:
        print('i = ', i, 'n = ',n)
        i = i * 2

def trickyBigO(n, m):
    i = m

    while (i > 100): 
        i = i / 3
    
    k = int(i)
    j = 1 
    for k in range(k, 0, -1):
        j = 1
        while j < n:
            print("Tricky j", j)
            j = j * 2
    

trickyBigO(100, 1000)