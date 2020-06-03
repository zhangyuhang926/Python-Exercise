import sys

def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n // 2
    L, R = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    n_l, n_r = len(L), len(R)
    L.append(sys.maxsize)
    R.append(sys.maxsize)
    new_arr = []
    i, j = 0, 0
    while i < n_l or j < n_r:
        if L[i] <= R[j]:
            new_arr.append(L[i])
            i += 1
        else:
            new_arr.append(R[j])
            j += 1
    return new_arr

list1 = [2,4,9,5,4,7,3,6]

print(merge_sort(list1))