# n = int(input())
n = 5
m = n//2 + 1
# print(m)
for i in range(1, n+1):
    for j in range(1, n+1):
        if i==j:
            if i<m:
                print("%d"%(n-i+1), end=" ")
            else:
                print("%d"%i, end=" ")
        elif i+j == n+1:
            if i<m:
                print("%d"%i, end=" ")
            else:
                print("%d "%j, end=" ")
        else:
            print("  ", end=" ")
    print('\n')