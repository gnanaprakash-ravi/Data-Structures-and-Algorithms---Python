n = 5

stars = 1
spaces = (n-1) * 2

for i in range(1, 2*n + 1):
    print('*' * stars, end="")
    print(" " * spaces, end="")
    print('*' * stars)
    
    if i < n:
        stars += 1
        spaces -= 2
    if i == n:
        pass
    if i > n:
        stars -= 1
        spaces += 2