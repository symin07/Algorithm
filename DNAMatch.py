
def dna_match_topdown(DNA1, DNA2):
    arrayCache = [[None for col in range(len(DNA2)+1)] for row in range(len(DNA1)+1)]  
    return topdownHelper(DNA1, DNA2, len(DNA1) -1 , len(DNA2) - 1, arrayCache)
def topdownHelper(str1, str2, m, n, arrayCache):
    # cache = np.matrix(i,j)
    #if i < 0 and j < 0:
    #    return arrayCache[len(DNA1)][len(DNA2)]
    matchNum = 0
    if m < 0 or n < 0:
        return 0
    if arrayCache[m+1][n+1] is not None:
        return arrayCache[m+1][n+1]
    if str1[m] == str2[n]:
            matchNum = 1 + topdownHelper(str1, str2, m-1, n-1, arrayCache) 
    elif str1[m] != str2[n]:
            matchNum = max(topdownHelper(str1, str2, m-1, n, arrayCache), topdownHelper(str1, str2, m, n-1, arrayCache))
    arrayCache[m+1][n+1] = matchNum
    return arrayCache[m+1][n+1]

def dna_match_bottomup(DNA1, DNA2):
    ac = [[0 for j in range(len(DNA2)+1)] for i in range(len(DNA1)+1)]  
    return bottomupHelper(DNA1, DNA2, len(DNA1), len(DNA2), ac)



def bottomupHelper(str1, str2, m, n, ac):
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if i == 0 or j ==0:
                ac[i][j] = 0
            if str1[i - 1] == str2[j - 1]:
                ac[i][j] = 1 + ac[i-1][j-1]
            else:
                ac[i][j] =max(ac[i - 1][j], ac[i][j-1])
    return ac[m][n]



DNA1 = "ATAGTTCCGTCAAA"
DNA2 = "GTGTTCCCGTCAAA"

print("Top Down Approach:", dna_match_topdown(DNA1, DNA2))
print("Bottom up Approach:", dna_match_bottomup(DNA1, DNA2))