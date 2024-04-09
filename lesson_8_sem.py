# Задача №31. 
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 8
# Задание необходимо решать через рекурсию

# Решение:

# def fib(n):
#     if n == 0 or n == 1:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# n = int(input())

# print(fib(n-2))

# ---------------------------------------------------------------------------------------

# Задача №33.
# Хакер Василий получил доступ к классному журналу и максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# Решение:

# n = int(input())
# list_1 = list()
# for i in range(n):
#     x = int(input())
#     list_1.append(x)

# max_n = max(list_1)
# min_n = min(list_1)

# for i in range(len(list_1)):
#     if list_1[i] == max_n:
#         list_1[i] = min_n

# print(list_1)

# ---------------------------------------------------------------------------------------

# Задача №35. 
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 

# Решение:

# def prime(n):
#     flag = True
#     i = 2
#     while i < n and flag: 
#         if n % i == 0:
#             flag = False

#         i += 1
#     if flag:
#         return 'yes'
#     else:
#         return 'no'
# n = int(input())
# print(prime(n))    

# ---------------------------------------------------------------------------------------

# Задача №37. 
# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

# Решение:

# будем использовать рекурсию

def f(n):
    if n == 0:
        return ''
    k = int(input())
    return f(n-1) + f'{k}'

n = int(input())
print(f(n))






