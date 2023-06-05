import timeit
'''
Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива
Ввод:
7
3 1 3 4 2 4 12
6
4 15 43 1 15 1
Вывод:
3 3 2 12
(каждое число вводится с новой строки
'''
# def task_k(first_array,second_array):
#     return [x for x in first_array if x not in second_array]


# print(task_k([3,1, 3, 4, 2, 4, 12],[4, 15, 43, 1, 15, 1]))


'''
Задача No41. Решение в группах
Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество элементов в массиве Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.
Ввод: Ввод:
55
1 2 3 4 5 15151
Вывод: Вывод:
02
'''


# def task41(array):
#     new_array = []
#     for y ,x in enumerate(array,1):
#         if y != len(array) and y+1 !=len(array):
#             if array[y] > array[y-1] and array[y] > array[y+1]:
#                 new_array.append(array[y])
#     return len(new_array)


# print(task41([1, 5, 1, 5, 1]))

# def task41(array):
#     return len([x for x,y in enumerate(array,1) if array[x-1:x] < array[x:x+1] > array[x+1:x+2]])


# print(task41([1, 5, 1, 5, 1, 1]))


'''

Задача No45. Решение в группах
Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
Ввод: Вывод:
300 220 284
10 минут

'''
def task45(k: int) -> set:
    # Перебираем все числа до 300, для каждого числа находим его делители x % i, суммируем и делаем словарь, где ключ являеться числом, а значение сумма его делителей.
    d = [{x :  sum([i for i in range(1,x) if x % i == 0])} for x in range(2,k) if k % 2 == 0]  
    # Перебираем список словарей, в словарях делаем проверку значений не равные 0 и 1, меньше числа k и ключь не равен 1, получаем кортежи из пар, ключь - значение
    s = [ i for x in d for i in x.items() if i[1] not in [0,1] and i[1] <= k and i[0] != i[1]]
    # Перебираем список кортежей с проверкой, если перевёрнутый элемент есть в списке s
    b = [x for x in s if x[::-1] in s]
    return [y for x,y in enumerate(b) if b[x] == tuple(i for z in b[x+1:x+2] for i in z)[::-1]]

# print(timeit.timeit(lambda: task45(100000),number=1)) # явно быстрей работает
print(task45(3000)) # явно быстрей работает


def task45(k: int) -> set:
    option = [x for x in range(1 ,k) if x >= 10 and (d := sum([i for i in range(1,x) if x % i == 0])) != x == sum([z for z in range(1,d) if d % z == 0 ])]  
    return option

print(task45(3000))
# print(timeit.timeit(lambda: task45(30000),number=1))

'''
Решение в группах
Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список чисел. Все числа списка находятся на разных строках.
Ввод: Вывод:
1232 3 2
15 минут

'''
from collections import Counter
def task43(array):
    return len([x for x,y in dict(Counter([sum(z) for z in set([(y,i) for x,y in enumerate(array) for i in array[1:]])])).items() if y > 1])


print(task43([1, 2, 3, 2, 3]))