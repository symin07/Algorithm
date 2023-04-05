# we can implement adjacency list using set in python
a, b, c, d, e, f = range(6)    # definition of node
N = [{b,c,d,f}, {a,d,f}, {a, b, d, e, f}]       # definition of set
print("Test adjaceny list of a, b, c, d, e, f = range(6): N=[{b, c, d, f}, ....]")
print("b in N[a]", b in N[a])
print("f in N[c]", f in N[c])
print("b in N[b] expected False: ", b in N[b])
print(len(N[c]))
print("print f of a, b, c, d, e, f:   ", f)
print(N[c])
print("End of Adjacency List")



# We can implement adjacency list using list in python
# In this case, we can traverse N in every node V
a, b, c, d, e, f = range(6) # 6 node
N = [[b, c, d, f], [a,d,f], [a, b, d, e], [a, e], [a, b, c], [b, c, d, e]]
print("Test adjaceny list using list of a, b, c, d, e, f = range(6): N=[{b, c, d, f}, ....]")
print("b in N[a]", b in N[a])
print("f in N[c]", f in N[c])
print("b in N[b] expected False: ", b in N[b])
print(len(N[c]))
print("print f of a, b, c, d, e, f:  ", f)
print(N[c])
print("End of Adjacency List")


