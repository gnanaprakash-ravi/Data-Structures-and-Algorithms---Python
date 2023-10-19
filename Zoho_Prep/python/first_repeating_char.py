# s = 'acdefbcdef'
# s = 'aaaaa'
# s = 'abcde'
s = 'baab'
    

hm = {}

for i in range(len(s)):
    if s[i] in hm:
        print(s[i])
        hm[s[i]] += 1
        break
    else:
        hm[s[i]] = 1

# for i in range(len(s)):
#     if hm[s[i]] != 1:
#         print(s[i])
#         break