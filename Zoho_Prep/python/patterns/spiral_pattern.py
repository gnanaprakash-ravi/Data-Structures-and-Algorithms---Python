# n = int(input())
# m = int(input())

n = 3
m = 3

fibolist = []

def fibo(n):
    if n == 1 or n == 0:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

for i in range(n*m):
    fibolist.append(fibo(i))
    
Mat = [[0]*m for _ in range(n)]
print(fibolist)
rowend = n
columnend = m

rowstart = 0
columnstart = 0
f = 0

while rowstart < rowend and columnstart < columnend:
    for i in range(columnstart, columnend):
        Mat[rowstart][i] = fibolist[f]
        f += 1
    rowstart += 1

    for i in range(rowstart, rowend):
        Mat[i][columnend - 1] = fibolist[f]
        f += 1
    columnend -= 1

    if rowstart < rowend:   #very important
        for i in range(columnend - 1, columnstart - 1, -1):
            Mat[rowend - 1][i] = fibolist[f]
            f += 1
        rowend -= 1

    if columnstart < columnend: #very important
        for i in range(rowend - 1, rowstart - 1, -1):
            Mat[i][columnstart] = fibolist[f]
            f += 1
        columnstart += 1
        
for row in Mat:
    print(row)