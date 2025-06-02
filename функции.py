# # n = 5, 6, 7, 8, 10, 12
# # b = 3, 4, 5, 2, 6, 7
#
# n = 5
# b = 3
# s = ''
# while n != 0:
#     ost = str(n % b)
#     s = s + ost
#     n = n//b
# print(s[::-1])
# len()
# sum()
# max()
# n = 6
# b = 4
# s = ''
# while n != 0:
#     ost = str(n % b)
#     s = s + ost
#     n = n//b
# print(s[::-1])

# def имя_функции(аргументы):
#    код
#    return значение

# написать функцию для перевода числа n в сс b

def perevod(n, b):
    s = ''
    while n > 0:
        ost = n % b
        s = s + str(ost)
        n = n // b
    # print(f'вывелось = {s[::-1]}')
    return s[::-1]


# # n = 5, 6, 7, 8, 10, 12
# # b = 3, 4, 5, 2, 6, 7

# x = 1000
# while x != 0:
#     x = int(input('Введите число: '))
#     y = int(input('Введите основание: '))
#     num = perevod(x, y)
#     print(f'переведенное число = {num}')

x = int(input('Введите число: '))
y = int(input('Введите основание: '))
num = perevod(x, y)
print(f'переведенное число = {num}')