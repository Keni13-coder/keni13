import timeit
# # from itertools import groupby

# # array = [1,22,55,1,1,44,23,22,13]

# # print([f'{x}:{list(y)}' for x,y in groupby(array)])

# def fib(num: int) -> int:
#     # 5 * (5-1) * (5-1(-1)) * (5-1(-1(-1))) * (5-1(-1(-1(-1))))
#     # 5 *  (4   *  3  *   2  *  1)
#     return num if num == 1 else num * fib(num-1)
# # print(fib(5))


# def suma(a: int, b: int):
#     return b if b == 0 else a + suma(a, b -1)

# '''
# suma(2,2)
#   2 + suma(2,1)
#         2 + sum(2, 0)
#                 if b == 0
#                     return  0



# '''

# # print(suma(2,2))

# """
#         2 2
#         /   \
#     2 1    2 2 
#     /    \
#   2 0   2 1
#   /  \
#  0    2 0
# """

# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]
#         greater = [i for i in array[1:] if i > pivot]
#         # print(pivot)
#         print(f'LEss {less}')
#         print(f'GReater {greater}')
#         return quick_sort(less) + [pivot] + quick_sort(greater)    
    
    
# # 1 запуск less = [5,2] +  pivot = [10] +  greater = []
# # Заходим в рекурсию quick_sort(less)
# # quick_sort(array) array = less = [5,2]
# # pivot = 5
# # less = [2]
# # greater = []
# # return quick_sort([2]) + [5] + quick_sort([])
# # Заходим в рекурсию quick_sort(less) № 2
# # И отрабатывает условие длины списка <= 1
# # return less = [2]
# # рекурсия quick_sort(less) = [2] + [5] + [0]
# # Выход из рекурсии, складываем стеки
# # [2,5] + [10] + []
   
# # print(quick_sort([1,2,3]))    


def quick_search(num,array):
    if len(array) == 1 :
        return 'хуй'
    else:
        if num < array[len(array)//2]:
            right = array[len(array)//2:]
            return quick_search(num,right)
        elif num == array[len(array)//2]:
            return "есть"
        else:    
            left = array[:len(array)//2]
            return quick_search(num,left)

  
b = [10,20,30,50,2]
print(quick_search(2,b))
# print(f"{timeit.timeit( lambda :quick_search(2,b))}")
# def fast(num , array):
#     if num in array:
#         return [f'Индекс данного числа {y} = {x}' for x,y in enumerate(array)]
#     else:
#         return  'хуй'

# #0.19650879999971949
# print(f"{timeit.timeit( lambda :fast(2,b))}")