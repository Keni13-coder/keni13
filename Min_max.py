def max_min(*array):
    index = 0
    max = 0
    min = 0
    sum = 0
    while index < len(array):
        if array[index] < array[min]:
            min = index
            index += 1
        elif array[index] > array[max]:
            max = index
            index += 1
        else:
            index += 1
    
    if max > min:
        while array[max] != array[min+1]:
            sum += array[min+1]
            min += 1
        return sum    
    elif max < min:
        while array[max+1] != array[min]:
            sum += array[max+1]
            max += 1
        return sum        
    else:
        return sum
print(max_min(2,3,4,5,88,66,44,99,1))


# функция находящая сумму чисел между максимальным и минимальным значением
def max_min(array):
    return sum([ i for i in array if array.index(max(array)) + 1 != array.index(min(array)) and i !=max(array) and i != min(array)])
