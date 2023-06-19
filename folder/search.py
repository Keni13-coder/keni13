import timeit
'''
Быстрый поиск - бинарный поиск
'''

def binary_search(list,item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
print(binary_search(['Александар',"Адексей","Борис","Боба","Влад","Владимир","Дмитрий","Денис"],"Боба"))
'сравнение так же работают со строками от Unicode по заглавной букве'

print(ord('Б'))
def InterpolationSearch(lys, val):
    low = 0
    high = (len(lys) - 1)
    while low <= high and val >= lys[low] and val <= lys[high]:
        index = low + int(((float(high - low) / ( lys[high] - lys[low])) * ( val - lys[low])))
        if lys[index] == val:
            return index
        if lys[index] < val:
            low = index + 1;
        else:
            high = index - 1;
    return -1
'''
Фибоначи поиск

'''
def FibonacciSearch(lys, val):
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    while (fibM < len(lys)):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1;
    while (fibM > 1):
        i = min(index + fibM_minus_2, (len(lys)-1))
        if (lys[i] < val):
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif (lys[i] > val):
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else :
            return i
    if(fibM_minus_1 and index < (len(lys)-1) and lys[index+1] == val):
        return index+1;
    return -1

array = [x for x in range(1,100000)]
# print(timeit.timeit(lambda: binary_search(array,1),number=1))
# print(timeit.timeit(lambda: FibonacciSearch(array,1),number=1))
# print(timeit.timeit(lambda: InterpolationSearch(array,1),number=1))
# print(FibonacciSearch(array,34500))



