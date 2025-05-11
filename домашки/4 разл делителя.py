for n in range(178965, 178982 + 1):
    deliteli = []
    for d in range(1, int(n**0.5) + 1):
        if n % d == 0:
            deliteli.append(d)
            deliteli.append(n//d)
    if len(deliteli) == 4:
        print(deliteli)
