def perevod7(n):
    s = ''
    while n > 0:
        ost = str(n % 7)
        s = s + ost
        n = n // 7
    return s[::-1]



for x in range(1, 2300 + 1):
    n10 = 7**350 + 7**150 - x
    n7 = perevod7(n10)
    if n7.count('0') == 200:
        print(x)