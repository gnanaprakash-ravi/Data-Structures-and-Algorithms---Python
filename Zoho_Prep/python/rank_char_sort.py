
def bubblesort(ar, arr):
    n = len(ar)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                swapped = True
                ar[j], ar[j+1] = ar[j+1], ar[j]
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not swapped:
            return

def mergesort(ar, arr):
    pass

rank = [5, 3, 4, 2, 1]
arr = ['b', 'a', 'c', 'd', 'e']

bubblesort(rank, arr)

for i in range(len(rank)):
    print('%d'%rank[i], end=" ")
print('\n')
for i in range(len(arr)):
    print('%c'%arr[i], end=" ")