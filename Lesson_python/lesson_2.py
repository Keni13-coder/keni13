from functools import reduce
"""
Задача No9. Решение в группах
По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * ... * N (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
Input: 5
Output: 120
"""

# def fact(num):
#     x = 1
#     summ = 1
#     while x <= num:
#         summ *= x
#         x += 1
#     return summ


# print(fact(5))

#рекурсивный метод
# def facts(num):
#     return  num * facts(num-1) if num != 0 else 1

# print(facts(5))


'''
Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, 
выведите число -1.
Input: 5 Output: 6
'''

'''
from itertools import islice

def fib(a=0, b=1):
    yield a
    while True:
        yield b
        a, b = b, a + b

fibonacci_numbers = list(islice(fib(), 20))
print(fibonacci_numbers)
'''
from math import sqrt
def fibonacci(n):
    arr = [0] * (n)
    arr[1] = 1
    for i in range(2, n):
        arr[i] = arr[i - 1] + arr[i - 2]
        # сделать обычный фиб с  добавление по условию x,y enumerate(array) array[y]<n
    return arr

print(fibonacci(5))

fib = lambda n: fibonacci(n) if sqrt(5*(n**2)-4)%1 == 0 or sqrt(5*(n**2)+4)%1 == 0 else -1
print(fib(5))

# a = int(input('введите a: '))
# f1 = 0
# f2 = 1
# fn = 0
# x = 0
# n = 3
# while fn <= a:
#     fn = f1 + f2
#     x = f2
#     f1 = x
#     f2 = fn
#     if fn == a:
#         print(n)
#         break
#     n += 1
# else:
#     print(-1)


'''
Задача No13. Решение в группах
Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел.
Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50
Input: 6 -> -20 30 -40 50 10 -10 Output: 2
'''

# Y = int(input("Введите количество дней: "))
# bufer = 0
# countd = 0
# county = 0

# while county <= Y:
#     N = int(input("Введите температуру дня: "))
#     county = county + 1
#     if(N > 0):
#         countd = countd + 1
        
#         if (bufer < countd):
#             bufer = countd
#     else:
#         countd = 0
# print('Самое теплое количество дней ', bufer)




# def task13(N,array):
#     count = 0
#     max_count = 0
#     z =[1 if x >0 else 0 for x in array]
#     for x in z:
#         if x > 0:
#             count +=1
#             if count > max_count:
#                 max_count = count
#         else:
#             count = 0        

#     return  max_count


# print(task13(6,[20, 30, -40, 50, 10, -10]))



# [0, 1, 0, 1, 1, 0]


