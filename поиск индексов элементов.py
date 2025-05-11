import random

lst = [random.randint(1, 4) for i in range(10)]
print(lst)

# перебор по элементам
for i in lst:
    print(i)

# перебор по индексам
for i in range(len(lst)):
    print(lst[i])

for i in range(len(lst)):
    if lst[i] == 1:
        print(i)

lst = []
for i in range(1, 10 + 1):
    lst.append(i**2)

print(lst)