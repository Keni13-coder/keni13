'''
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной
.Выведите минимальное количество монет, которые нужно перевернуть
'''
# Честно я не совсем понял задание. Откуда берётся информация о расположении монет.
# Если ифнформацию о монетах превратить в массив, то получаться так:

def task10(N,array_money):
    # return array_money.count(0) if array_money.count(1) > array_money.count(0) else array_money.count(1)
    return min(sum(array_money),N-sum(array_money))



print(task10(5,[1,0,0,0,0]))