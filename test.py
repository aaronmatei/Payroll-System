def getMinimumCost(n,k, c):
    cost = 0
    c = sorted(c, reverse=True)
    for i in range(0, n):
        cost += (i // k + 1) * c[i]
    return cost
print(getMinimumCost(5,3,[1,3,5,7,9]))