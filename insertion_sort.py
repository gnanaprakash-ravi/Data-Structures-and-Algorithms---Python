def insertionsort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -=1

arr = [21, 38, 29, 17, 4, 25, 11, 32, 9]
insertionsort(arr)
print(arr)
