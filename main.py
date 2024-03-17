# a = 5
# b = 5.89
# c = 'hello'
# print (f"{a} - {b} - {c}")
# print("{} - {} - {}".format(a,b,c))

# print('Введите первую строку')
# a = input()
# b = input('Введите второе число: ')
# print(a+b)
# print(a, '+', b, '=', a + b)


# c = 5.89
# print(c)
# print(type(c))

# c = int(c)  # с помощью присваивания переменной С типа int, можно получить целое число из дробного
# print(c)
# print(type(c))

# c = str(c)  # переменной С присвоили строковый тип данных
# print(c)
# print(type(c))


# # округление чисел
# a = 5.7609
# b = 6.4980
# print(round(a*b,3))

# a = 1 > 4
# print(a) # False
# —------------------------------------
# a = 1 < 4 and 5 > 2
# print(a) # True
# # —------------------------------------
# a = 1 == 2
# print(a) # False
# # —------------------------------------
# a = 1 != 2
# print(a) # True

# a = 'qwe'
# b = 'qwe'
# print(a == b) # True

# a = 1 < 3 < 5 < 10
# print (a) # True

n = int(input())
flag = True
i = 2
while flag:
    if n % i == 0: # если остаток при делении числа n на i равен 0
        flag = False
        print(i)
    elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
        print(n)
        flag = False
    i += 1

    