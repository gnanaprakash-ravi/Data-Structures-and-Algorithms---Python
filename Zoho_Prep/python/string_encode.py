s = 'aabbccc'

count = 1
ans = ""

for i in range(1, len(s)):
    if s[i-1] != s[i]:
        ans = ans + s[i-1]
        ans = ans + str(count)
        count = 1
    else:
        count += 1
    
ans = ans + s[-1]
ans = ans + str(count)
print(ans)