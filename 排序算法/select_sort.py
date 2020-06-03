import random

def selectSort(arr):
    N = len(arr)
    for i in range(N):
        min = i
        for j in range(i+1, N):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

a = [i for i in range(1, 11)]
random.shuffle(a)
print(a)
print(selectSort(a))
