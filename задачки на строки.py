# "Иван:25,Мария:30,Петр:20,Анна:28"
# Имя: имя, возраст: возраст
s = "Иван:25,Мария:30,Петр:20,Анна:28"
data = s.split(',')
print(data)
for i in data:
    a = i.split(':')
    # name = a[0]
    # age = a[1]
    name, age = a
    print(f'Имя: {name}, возраст: {age}')

# name, age = ['Иван', '25']
# print(name)
# print(age)


