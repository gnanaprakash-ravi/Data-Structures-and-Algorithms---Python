def bubblesort(ele):
    size = len(ele)
    
    for a in range(size-1):
        swapped = False
        for i in range(size -1 -a):
            if ele[i] > ele[i+1]:
                ele[i], ele[i+1] = ele[i+1], ele[i]
                swapped = True
        if not swapped:
            break

elements = [5,9, 2, 1, 67, 34, 88, 34]
bubblesort(elements)
print(elements)