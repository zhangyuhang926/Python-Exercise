def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [45,23,56,2,76,3,5]
bubbleSort(arr)
print("排序后的数组：")
for i in range(len(arr)):
    print("%d" %arr[i])