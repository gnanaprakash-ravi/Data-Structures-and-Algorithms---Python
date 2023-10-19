# n = int(input("Enter an odd number: "))
n = 9

if n & 1 == 0:
    print("Enter only an odd number")
else:
    outside_space = n // 2
    inside_space = 1
    for i in range(n):
        # spaces
        for j in range(outside_space):
            print(' ', end='')
        if i < n // 2:
            outside_space -= 1
        else:
            outside_space += 1
        
        # star
        if i == 0 or i == n - 1:
            print("*")
        else:
            # star 1
            print("*", end='')
            # space
            for j in range(inside_space):
                print(" ", end='')
            if i < n // 2:
                inside_space += 2
            else:
                inside_space -= 2
            # star 2
            print("*")
