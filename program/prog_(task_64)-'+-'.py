def max_sequence(ar):
    if ar:
        if any(map(lambda x: x >= 0,ar)):
            rezul = sum(ar)
            # a = [sum(ar[i:j]) for i,_ in enumerate(ar) for j,_ in enumerate(ar,i)]
            for i,_ in enumerate(ar):
                for j,_ in enumerate(ar,i):
                    if sum(ar[i:j]) > rezul:
                        rezul = sum(ar[i:j])
            return rezul
        return 0
    return 0

# print(max_sequence([]))
# print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))





# Функция для нахождения максимальной суммы смежного подмассива
# в заданном целочисленном массиве
def kadane(arr):
# сохраняет подсписок максимальной суммы, найденный на данный момент, итоговый результат 
    max_so_far = 0  
# сохраняет максимальную сумму подсписка, заканчивающегося в текущей позиции, для сравнения в цикле
    max_ending_here = 0
 
# пройтись по заданному списку
    for i in arr:
        # обновите максимальную сумму подсписка, "заканчивающегося" индексом "i" (путем добавления
        # текущего элемента к максимальной сумме, заканчивающейся предыдущим индексом "i-1")
        max_ending_here = max_ending_here + i
 
        # если максимальная сумма отрицательна, установите ее равной 0 (что представляет
        # пустой подсписок)
        max_ending_here = max(max_ending_here, 0)
 
        # обновите результат, если окажется, что текущая сумма подсписка больше
        max_so_far = max(max_so_far, max_ending_here)
 
    return max_so_far
 
 
if __name__ == '__main__':
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(kadane(arr))