# s = str(input())
s = 'a11b12c2'
temp = ''
num = 0

i = 0
while(i<len(s)):
    if s[i].isdigit():
        temp = s[i-1]
        
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
            
        for j in range(num):
            print(temp, end="")
            
        num = 0
    i += 1

print()