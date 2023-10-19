arr = [11, 31, 4, 3, 9]

odd = []
even = []

for i in range(len(arr)):
    if i & 1 == 0:
        odd.append(arr[i])
    else:
        even.append(arr[i])
        
odd = sorted(odd, reverse=True)
even = sorted(even)

output = [0] * len(arr)
oi = 0
ei = 0

for i in range(len(arr)):
    if i%2 == 0:
        output[i] = odd[oi]
        oi += 1
    else:
        output[i] = even[ei]
        ei += 1

print(output)