# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 0,56 -> 11


num = input('Введите вещественное число: ')
sum = 0

for i in num:
    if i.isdigit():
        sum += int(i)

print(sum)



# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


n = int(input('Введите число: '))
fact = 1
for i in range(n):
    fact *= i+1
    print(fact, end=' ')


# 3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

n = int(input())
lst = [round((1+1/i)**i, 2) for i in range(1, n+1)]
print(f'Для n={n} {lst}\nСумма: {sum(lst)}')


# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0


input_num = int(input('Введите число N: '))
list_n = []
for i in range(input_num*-1, input_num+1):
    list_n.append(i)

print(list_n)

input_ind = list(map(int, input('Введите индексы для нахождения произведения (Индексы вводятся одной строкой, через пробел): ').split()))
print(input_ind)

result = 1
for i in input_ind:
     print (list_n[i], ' * ' , end='' )
     result *= list_n[i]

print('= ', result)



# 5. Реализуйте алгоритм перемешивания списка.

import random

input_num = int(input('Введите число N: '))
listA = []
for i in range(input_num*-1, input_num+1):
    listA.append(i)

print(listA)

random.shuffle(listA)

print(listA)


