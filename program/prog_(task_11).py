# from heapq import nsmallest
# Нахождение 2 минимальных чисел из массива
# def sum_two_smallest_numbers(numbers):
#     return sum(nsmallest(2, numbers))
        

# print(sum_two_smallest_numbers([8, 8, 12, 18, 22 ]))

def sum_min(array):
    first = array[0]
    second = array[0]
    for index, value in enumerate(array):
        if array[index] < first:
            if second != first:
                second= first
            first = array[index]
        else:
           if array[index] < second:
                second = array[index]    
    return first + second           

print(sum_min([8, 5,18, 3,7]))


