'измениемые типы данных после похождение функций так же меняются'
'''ar = [1,2,3,4,5]
def t(ar):
    ar[1::2]=1,1
    return ar
print(ar,t(ar))
[1, 1, 3, 1, 5] [1, 1, 3, 1, 5]

'''
'наименованные аргументы должны быть не изменяемыми, так как после каждого вызова функций список будет пополняться'
'''
def t(a,b=[])
    b.append(a)
    return b
prunt(t(1))
b = [1]
prunt(t(1))
b = [1,1]
'''

'def t(*,key)- * говорит о  том что после неё могут быть только ключевые аргументы'
'def t(arg,/)- / говорит о том что аргуметы до неё могут быть только позиционными'

'*args-все элементы = tuple,**kwargs-все элементы = dict'

'''Задание №2
 Напишите функцию, которая принимает строку текста. 
✔ Сформируйте список с уникальными кодами Unicode каждого 
символа введённой строки отсортированный по убыванию.

'''

def task_2(st:str)->list[int]:
    # return sorted(set((ord(x) for x in st)),reverse=True)
    return sorted(map(ord,set(st)),reverse=True)


# print(task_2('Сформируйте список с уникальными кодами'))

'''
Задание №3
✔ Функция получает на вход строку из двух чисел через пробел. 
✔ Сформируйте словарь, где ключом будет 
символ из Unicode, а значением — целое число. 
✔ Диапазон пар ключ-значение от наименьшего из введённых 
пользователем чисел до наибольшего включительно.
'''

def task_3(st:str) ->dict:
    st = sorted(map(int,st.split()))
    start,end = st[0],st[1]+1
    return {chr(x):x for x in range(start,end)}

# print(task_3('100 20'))


'''
Задание №4
✔ Функция получает на вход список чисел. 
✔ Отсортируйте его элементы in place без использования 
встроенных в язык сортировок. 
✔ Как вариант напишите сортировку пузырьком. 
Её описание есть в википедии.
'''
def task_4(ar:list)-> None:
    for _ in range(len(ar)-1):
        for i,v in enumerate(ar):
            if i != 0:
                if ar[i] < ar[i-1]:
                    ar[i-1],ar[i] =ar[i],ar[i-1]
        

               
# array = [29,19,47,11,6,19,24,12,17,23,11,71,41,36,71,13,18,32,26]
# task_4(array)
# print(array)
'''Задание №5
Функция принимает на вход три списка одинаковой длины:
✔ имена str, 
✔ ставка int, 
✔ премия str с указанием процентов вида «10.25%».
✔ Вернуть словарь с именем в качестве ключа и суммой 
премии в качестве значения. 
✔ Сумма рассчитывается как ставка умноженная на процент премии. 
'''

def task_5(first_ar:list,second_ar:list,third_ar:list)-> dict:
    return {x[0]:x[1] / 100 * float(x[2]) for x in zip(first_ar,second_ar,map(lambda x:x.replace('%', ''),third_ar))}


print(task_5(["миша","паша","саша"],[35000,45000,40000],['10.25%','15.25%','8.25%']))

'''
Задание №6
✔ Функция получает на вход список чисел и два индекса. 
✔ Вернуть сумму чисел между между переданными индексами. 
✔ Если индекс выходит за пределы списка, сумма считается 
до конца и/или начала списка.

'''


def task_6(arr:list,start_index:int,end_index:int)->int:
    return sum(arr[start_index+1:end_index])



print(task_6([29,19,47,11,6,19,24,12,17,23,11,71,41,36,71,13,18,32,26],-160,198))


'''Задание №7
Функция получает на вход словарь с названием компании в качестве ключа 
и списком с доходами и расходами (3-10 чисел) в качестве значения. 
✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании 
прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
'''
dit = {"пидор":[100,-100,10],
       "Молодец":[100,-100,10],
       "чулбус":[200,-200,10],}
def task_7(di:dict)->bool:
    return all(sum(v)>0 for k,v in di.items())


print(task_7(dit))