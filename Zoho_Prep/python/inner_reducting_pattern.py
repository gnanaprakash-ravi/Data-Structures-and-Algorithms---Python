# n = int(input())
n = 4

size = n*2 - 1
front = 0
last = size-1

M = [[0] * size for _ in range(size)]

while (n != 0):
    for i in range(front, last+1):
        for j in range(front, last+1):
            if (i == front or i == last or j == front or j == last):
                M[i][j] = n
    
    front += 1
    last -= 1
    n -= 1
    
# for i in M:
#     print(i)
    

for i in range(size):
    for j in range(size):
        print(M[i][j], end="  ")
    print('\n')