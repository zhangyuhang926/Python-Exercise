def findKthLargest(L, K):
    size = len(L)
    L.sort()
    return L[size - K]

L = [2,1,4,3,2,5]
K = 2
print(findKthLargest(L, K))
