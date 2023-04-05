strGlobal = ""
# this code is by min: Big(n^2)
def longComSeq(str1, str2, num):
    if len(str1) == 0:
        return num
    for char in str2:
        if str1[0] == char:
            return longComSeq(str1[1:], str2, num+1)
    return longComSeq(str1[1:], str2, num)    

# this code is for lsc_BF

def lcs_BF_helper(s1, s2, m,n):
    
    if m < 0 or n < 0:
        return 0
    elif s1[m] == s2[n]:
        global strGlobal
        strGlobal = strGlobal + s1[m]        
        return 1 + lcs_BF_helper(s1, s2 , m-1, n-1)
    else:
        return max(lcs_BF_helper(s1, s2, m-1 , n), lcs_BF_helper(s1, s2, m, n-1))

def lcs_BF(str1, str2):
    return lcs_BF_helper(str1,str2, len(str1)-1, len(str2)-1)

def lcs_term(str1, str2):
    if len(str1) <= 0 or len(str2) <= 0:
        return 0
    elif str1[0] == str2[0]:
        return 1 + lcs_term(str1[1:], str2[1:])
    else:
        return max(lcs_term(str1[1:], str2), lcs_term(str1, str2[1:]))







str1 = "efdbe"
str2 = "edcba"
print(longComSeq(str1, str2, 0))

# this code is for lsc_BF
print(lcs_BF(str1, str2))
print(lcs_term(str1, str2))



