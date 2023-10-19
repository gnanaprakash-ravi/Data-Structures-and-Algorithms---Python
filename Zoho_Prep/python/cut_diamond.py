# n = int(input("Enter a number: "))
n = 7

stars = n // 2 + 1  # if 7, stars = 4
spaces = 0

for i in range(1, n + 1):
    print("*" * stars, end="")
    print(" " * spaces, end="")
    print("*" * stars)
    
    if i < n // 2 + 1:
        stars -= 1
        spaces += 2

    if i == n // 2 + 1:
        stars = 2
        spaces = n - 3

    if i > n // 2 + 1:
        stars += 1
        spaces -= 2