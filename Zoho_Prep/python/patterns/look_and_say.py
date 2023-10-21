# n = int(input("Enter the number: "))
n = 2
print(1)
s = "1"
i = 1

while i < n:
    new_s = ""
    count = 1
    a = s[0]

    for j in range(1, len(s)):
        if s[j] != s[j - 1]:
            print(count, a, sep="", end="")
            new_s += str(count) + a
            a = s[j]
            count = 1
        else:
            count += 1

    print(count, a, sep="", end="\n")
    new_s += str(count) + a
    s = new_s
    i += 1