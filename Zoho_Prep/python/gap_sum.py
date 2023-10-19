arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(arr)
gap = 3

for i in range(0, gap):
    sum = 0
    for j in range(i, n, gap):
        sum += arr[j]

    print(sum, end=" ")