def amount(A, S):
    amountHelper(A, S, [[]], [], len(A), 0)

def amountHelper(A, S, rst, combi, rm, idx):
    if not A: 
         return A
    if sum(combi) == S:
        return True
    elif sum(combi) > S:
        return False
    elif rm <= 0:
        return False
    elif idx >= len(A):
         idx = len(combi)

    combi.append(A[idx])
    if(amountHelper(A, S, rst, combi, rm, idx+1)):
        rst.append(combi)
        
    else:
        idx = idx + 1
        combi.pop()
    
    if(amountHelper(A, S, rst, combi, rm, idx)):
        rst.append(combi)
    else: 
        idx = len(combi)
        combi.pop()    

    return rst
    # return rst

print(amount([11,1,3,2,6,1,5], 8))