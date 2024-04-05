# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть
# Ввод  5 -> 1 0 1 1 0
# Вывод 2

# Решение:

# coins = [0, 1, 0, 1, 1, 0]
# zero = 0
# one = 0
# for i in range(len(coins)):
#     if coins[i] == 0:
#         zero += 1
#     if coins[i] == 1:
#         one += 1
# if zero >= one:
#     print(one)
# else:
#     print(zero)


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3


# Решение:
# s = 12
# p = 27
# for X in range (1, 1001):
#     for Y in range (1, 1001):
#         if X + Y == s and X * Y == p:
#             if X <= Y:
#                 print (X,Y)
#             else:
#                 break



# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числавида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

n = 32
k = 0
while 2**k <= n:
    print (2**k)
    k += 1