class DisjSet:
    def __init__(self, n):
        #construct to create and ititialize set of n items
        self.rank = [1]*n
        self.parent = [i for i in range(n)]

    # Finds set of given item x
    def find(self, x):
        #finds the representive of the set that x is an element of
        if(self.parent[x] != x):
            # if x is not the parent of itself
            # then x is not the representive of its set,
            self.parent[x] = self.find(self.parent[x])

            # so we recursively call Find on its parent and move i's
            # node directly under the representive of this set
        
        return self.parent[x]
    
    #Do uninon of two sets represented by x and y.
    def Union(self, x, y):
        # Find current sets of x and y
        xset = self.find(x)
        yset = self.find(y)

        # If they are already in same set
        if xset == yset: return 

        # Put smaller ranked item under bigger ranked item 
        # if ranks are different
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset

        # If ranks are same, then y under x (doesn't matter which one goes where)
        # and increment rank of x's tree
        else: 
            self.parent[yset] = xset
            self.rank[xset] = self.rank[xset] + 1


# Driver code
obj = DisjSet(5)
obj.Union(0, 2)
obj.Union(4, 2)
obj.Union(3, 2)
if obj.find(4) == obj.find(0):
    print('Yes')
else: 
    print('No')
if obj.find(1) == obj.find(0):
    print('Yes')
else: 
    print('No')    


def Kruskal(V, E):
    E_sorted = sort E by increasing weight
    for v in V: make_set(v)
    MST = {}
    for (u, v) in E_sorted:
        if(Find_set(u) != Find_set(v)):
            MST.add((u, v))
            Union(u, v)
    return MST
