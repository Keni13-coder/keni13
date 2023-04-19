snail_map = [[1, 2, 3, 4, 5],
           [6, 7, 8, 9, 10],
           [11, 12, 13, 14, 15], 
           [16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25]]
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
def snail(array):
    list_of_numbers = []
# Содаём цикл с условием нашего array где он перестанет рабоат когда будет break или закончиться список    
    while array:
# Добавляем в список элементы с первого array и после удоляем его    
        for i in array[0]:
            list_of_numbers.append(i)
        array.pop(0)
# делаем проверку чтоб не выходил за границы array так как используем индексацию -1       
        if not array:
            break
# Добавляем последний элемент каждого array в наш список и удаляем из array                    
        for j in array:
            list_of_numbers.append(j[-1])
            j.pop()
# Поиск обратных индексов и добавление по ним в наш список, после удаляем последний элемент array            
        for k in range(len(array[-1]) -1, -1, -1):
            list_of_numbers.append(array[-1][k])
        array.pop()
        if not array:
            break
#Переворачиваем array и из каждого его элемента добавляем первый элемент в наш список и удаляем этот элемент из array        
        for l in reversed(array):
            list_of_numbers.append((l[0]))
            l.pop(0)
    return list_of_numbers
print(snail(array))


# рекурсивная функция делает стеки
new_array =  [[6, 9], [5, 8], [4, 7]]
new_array_1 =[[8, 7], [5, 4]]
new_array_2 = [[4], [5]]
new_array_3 = [[5]]
# следующий шаг уходит в условие рекурсии if array else []
# после чего начинается сбор стеков array[0], где array[0] new_array_3[0],new_array_2[0],new_array_1[0],new_array[0]
#[1,2,3]
#[6,9]
#[8,7]
#[4]
#[5]
#[1, 2, 3, 6, 9, 8, 7, 4, 5]
def snails(array):
    return array[0] + snail(list(map(list, [*zip(*array[1::])][::-1]))) if array else []
print(snails(array))
