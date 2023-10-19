a = []
b = []
m = int(input())
n = int(input())

for i in range(m):
    x = int(input())
    a.append(x)

for j in range(n):
    y = int(input())
    b.append(y)

result = []
i = 0
j = 0
while(i<m and j<n):
    if (a[i] < b[j]):
        result.append(a[i])
        i += 1
    else:
        result.append(b[j])
        j += 1
while(i<m):
    result.append(a[i])
    i += 1
while(j<n):
    result.append(b[j])
    j += 1

print(result)