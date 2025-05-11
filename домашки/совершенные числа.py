n = int(input())
for i in range(1, n + 1):
    delits = []
    for d in range(1, int(i**0.5) + 1):
        if i % d == 0:
            delits.append(d)
            delits.append(i//d)
    if sum(delits) - i == i:
        print(i, delits)
