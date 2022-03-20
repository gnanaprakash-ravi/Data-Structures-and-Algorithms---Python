#%%
expense = [2200, 2350, 2600, 2130, 2190]
print("Extra spent on feb comp. to jan: ",expense[1]-expense[0])
first = 0
for i in expense[:3]:
    first += i
print("expense of first qua:", first)
print(2000 in expense)

expense.insert(5, 1980)
expense[3] = expense[3] + 200
print(expense)

#%%
heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

print(len(heros))
heros.append("black panther")
print(heros)
heros.remove("black panther")
heros.insert(3, 'black panther')
heros[1:3] = ['doctor strange']
print(heros)
print(sorted(heros))

#%%
max = int(input())
odd = []
for i in range(3, max+1):
    if i%2 !=0:
        odd.append(i)
print(odd)
