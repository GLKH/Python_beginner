# # 1й способ создания списков
# list_1 = []

# # 2й способ созадния списка через функцию list
# list_1 = list()

# # 3й способ  созадания списка через указание значений
# list_1 = [1,2,3,8]

# print(list_1) #печасть списка со скобочками, выдит так: [1,2,3,8]
# print(*list_1) #печасть списка без скобочек, выдит так: 1,2,3,8

# # вывод списка через операто for
# for i in list_1:
#     print(i)

# # вывод длины списка
# print('Длина списка list_1:', len(list_1))

# # вывод элемента списка
# print(list_1[2]) #вывод элемента с индексом 2, выведет число 3

# # вывод элемента списка
# print(list_1[-1]) #вывод элемента с индексом -1, выведет число 8, первый элемент справа

# # добавление элементов в списки
# list_1 = [1, 5]
# print(list_1)
# list_1.append(8)
# print(list_1)
# list_1.append(85)
# print(list_1)

# # заполнение пустого списка значениями от 0 до 4 через for
# list_2 = []
# print(list_2)
# for i in range(5):
#     list_2.append(i)
#     print(list_2)

# Основные действия со списками:

# 1. Удаление последнего элемента списка.
# Метод pop удаляет последний элемент из списка:
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop()) # 0
# print(list_1) # [12, 7, -1, 21]
# print(list_1.pop()) # 21
# print(list_1) # [12, 7, -1]
# print(list_1.pop()) # -1
# print(list_1) # [12, 7]


# 2. Удаление конкретного элемента из списка.
# Надо указать значение индекса в качестве аргумента функции pop:
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(0)) # 12
# print(list_1) # [7, -1, 21, 0]


# 3. Добавление элемента на нужную позицию.
#  Функция insert — указание индекса (позиции) и значения.
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.insert(2, 11)) # т.е. мы добавляем на 2-й индекс значение 11
# print(list_1) # [12, 7, 11, -1, 21, 0]

# Срез списка
# Помните в конце первой лекции Вы прошли срезы строк? Также существует срез списка,
# давайте научимся изменять наш список
# ● Отрицательное число в индексе — счёт с конца списка
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0]) # 1
# print(list_1[1]) # 2
# print(list_1[len(list_1)-1]) # 10
# print(list_1[-5]) # 6
# print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2]) # [1, 2]
# print(list_1[len(list_1)-2:]) #[9, 10]

# Срез списка
# Помните в конце первой лекции Вы прошли срезы строк? Также существует срез списка,
# давайте научимся изменять наш список
# ● Отрицательное число в индексе — счёт с конца списка
# print(list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9]
# print(list_1[6:-18]) # []
# print(list_1[0:len(list_1):6]) # [1, 7]
# print(list_1[::6]) # [1, 7]


# КОРТЕЖИ

# Кортеж — это неизменяемый список.
# Тогда для чего нужны кортежи, если их нельзя изменить? В случае защиты каких-либо
# данных от изменений (намеренных или случайных). Кортеж занимает меньше места в
# памяти и работают быстрее, по сравнению со списками
# t = () # создание пустого кортежа
# print(type(t)) # class <'tuple'>
# t = (1,)
# print(type(t))
# t = (1)
# print(type(t))
# t = (28, 9, 1990)
# print(type(t))

# # преобразования списка в кортеж
# v=[1,8,9]
# print(v)
# print(type(v))

# v= tuple(v)
# print(v)
# print(type(v))

# # разделение кортежа на элементы
# a,b,c = v
# print(a,b,c)


# t = (1,2,3,5)
# # print(t[1]) # вывод первого элемента кортежа


# # for i in t:
# #     print(i) # вывод всех элементов кортежа 

# for i in range(len(t)): # второй способ вывода всех элементов кортежа 
#     print(t[i])

# Кортежи
# Можно распаковать кортеж в независимые переменные:
# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))# r:red g:green b:blue


# СЛОВАРИ

# d = {} # создание словаря
# d = dict() # также создание словаря

# d['q'] = 'qwerty' # указываем ключ q, по которому мы выведем значение qwerty
# print(d) # выведется {'q': 'qwert'}, т.е. это означает что в словаре есть ключ q, по которому если обратимся, то получим 'qwerty'

# d['w'] = 'werty'
# print(d)

# print(d['q']) # вывод значений только по ключу q


# ниже примеры вызова значений по ключу и удаление элемента из словаря
# dictionary = {}
# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# # print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# # print(dictionary['left']) # ← типы ключей могут отличаться
# # print(dictionary['up']) # ↑ типы ключей могут отличаться
# # dictionary['left'] = '⇐'
# # print(dictionary['left']) # ⇐
# # print(dictionary['type']) # KeyError: 'type'
# # del dictionary['left'] # удаление элемента

# for item in dictionary:
#     print('{}: {}'.format(item, dictionary[item])) # вывод всех значений словаря в формате ключ:значение

# for (k,v) in dictionary.items():
#     print(k, v) # еще один способ вывода всех значений словаря в формате ключ:значение


# МНОЖЕСТВА (содержат уникальные заначения)

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')                              # при добавлении red, не происходит добавление, т.к. уже есть такое уникальное значение
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')                             # добавление элемента
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')                           # удаление элемента
# print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'  
# colors.discard('red') # ok            # удаление элемента с проверкой, если значение есть, то удаляет, если нет то ничего не происходит
# print(colors)
# colors.clear()                     # удаление всех элементов множества
# print(colors)

# # Операции со множествами в Python:
# a = {1, 2, 3, 5, 8}                      # первое множество a
# b = {2, 5, 8, 13, 21}                    # второе множество b
# c = a.copy() # c = {1, 2, 3, 5, 8}       # операция копирования множества a в с
# print(c)
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}    # операция объединения множества a с множеством b
# print(u)
# i = a.intersection(b) # i = {8, 2, 5}         # операция нахождения пересечений множества a с множеством b
# print(i)
# dl = a.difference(b) # dl = {1, 3}            # разность множества a и множества b (a-b)
# print(dl)
# dr = b.difference(a) # dr = {13, 21}          # разность множества b и множества a (b-a)
# print(dr)
# q = a.union(b).difference(a.intersection(b))  # {1, 21, 3, 13}    # сложная ф-ция, первым действием находится пересение мн-ва a с мн-вом b
# print(q)                                                          # затем объединение a и b, а затем разность объедиенеия с пересечением 

# #Неизменяемое или замороженное множество(frozenset) — множество, с которым не будут
# # работать методы удаления и добавления.
# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})


# List Comprehension - ГЕНЕРАТОР СПИСКОВ

# У каждого языка программирования есть свои особенности и преимущества. Одна из
# культовых фишек Python — list comprehension (редко переводится на русский, но можно
# использовать определение «генератора списка»). Comprehension легко читать, и их
# используют как начинающие, так и опытные разработчики. List comprehension — это
# упрощенный подход к созданию списка, который задействует цикл for, а также инструкции
# if-else для определения того, что в итоге окажется в финальном списке.

# 1. Простая ситуация — список:
# list_1 = [exp for item in iterable]

# 2. Выборка по заданному условию:
# list_1 = [exp for item in iterable (if conditional)]



# ЗАДАЧА 1 (на генерацию списков)
# Создать список, состоящий из четных чисел в диапазоне от 1 до 100

# Решение обычным путем (без функции "генераци списков"):
# list_1 = []
# for i in range(1,101):
#     list_1.append(i)
# print(list_1)

# # Решение с помощью "генераци списков":
# list_1 = [i for i in range(1,101)]
# print(list_1)



# ЗАДАЧА 2 (на генерацию списков)
# Создать список, состоящий из четных чисел в диапазоне от 1 до 100 с условием: только четные числа

# Решние:
# list_1 = [i for i in range(1,101) if i % 2 == 0]
# print(list_1)


# ЗАДАЧА 3 (на генерацию списков)
# Создать список, состоящий из четных чисел в диапазоне от 1 до 100 с условием: только четные числа, 
# а также создать пары каждому из чисел (кортежи)

# Решние:
# list_1 = [(i,i) for i in range(1,101) if i % 2 == 0]
# print(list_1)


# ЗАДАЧА 4 (на генерацию списков с умножением)
# Создать список, состоящий из четных чисел в диапазоне от 1 до 10, умноженных на 2, с условием: только четные числа, 

# Решние:
# list_1 = [i * 2 for i in range(10) if i % 2 == 0]
# print(list_1)