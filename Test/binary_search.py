from math import log
import timeit
def binary_search(num,array):
    min_len = 0
    max_len = len(array)-1 # 5
    while min_len <= max_len : # 5
        mid = (min_len + max_len) // 2 
        item = array[mid]
        if item == num:
            return mid
        if item >  num:
            max_len = (min_len + max_len) // 2  - 1
        else:
            min_len = (min_len + max_len) // 2  + 1 
            
    return None    

# b = [1, 3, 7, 9]                           
# print(binary_search(9,[1, 3, 6, 7, 9, 11,]))
# c = [10,20,2,30,50]
# print(f"{timeit.timeit( lambda :binary_search(2,c))}")
# Log 4_000_000_000 = 32
# log 1_000_000_000 = 30
# log 100 = 7
a = int(log(16,2))
print(a)              