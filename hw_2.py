# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

# n = int(input("Введите кол-во монеток: "))
# k = 0
# for i in range(n):
#     v = int(input())
#     if v == 1:
#         k += 1
# print(k if k<n/2 else n-k)


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# x = int(input('Введите первое натуральное число X от 1 до 1000: '))
# y = int(input('Введите второе натуральное число Y от 1 до 1000: '))
# S = x + y
# P = x * y
# if x < 1 or x > 1000 or y < 1 or y > 1000:
#     print('Вы ввели число не из заданного диапазона')
# else:
#     for i in range(1001):
#         for j in range(1001):
#             if (i * j == P) and (i + j == S):
#                         print(i, j)
#                         print(S, P)

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("Введите число: "))
k = 1
while k < n:
    print (k, end=" ")
    k = k * 2
                        
                        