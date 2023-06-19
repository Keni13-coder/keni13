'''
Задание 8
'''

def test(N):
    return [print('_' * (N-i) + '*' * (i+i+1)+ '_' * (N-i)) if i % 2 != 0 else print('_' * (N-i) + 'o' * (i+i+1)+ '_' * (N-i))  for i in range(N)]

# test(10)
'Задача 5'
def t_2(n,e):
    return sum(x for x in range(0,n,2) if x % e != 0)


# print(t_2(100,4))

'Задача 7'
# def t_3(n=input("Введите число от 1 до 999: ")):
    # A = 10
    # B = 100
    # while not n.isdigit() or int(n) > 999:
    #     n = input("Введите число от 1 до 999: ")      
    # n = int(n)
    # match n:
    #     case z if z < A:
    #         return (z**2)
    #     case z if z >= B:
    #         def dd(i):
    #             return i if i < A else str('' if (d := i % A) == 0 else d) + str(dd(i // A))
    #         return dd(z)
    #     case z if z > A <B:
    #         return (z+(z % A))

    
# print(t_3())

'задача 6'
def t_4(n):
    x = 4
    z = 100
    return 'Обычный' if n % x != 0 or n % z == 0 and n % (z*x) != 0 else 'Високосный'


# print(t_4(2100))

'задача 9'
def t_5():
    x = 10
    lis = [[f'{i} * {j} = {i*j}' for j in range(2,x+1)] for i in range(2,x)]
    [print(x) for x in zip(lis[0],lis[1],lis[2],lis[3])]
    print()
    [print(x) for x in zip(lis[4],lis[5],lis[6],lis[7])]

# t_5()


def dz(n):
    ZERO = 0
    FIRST = 1
    FIVE = 5
    FOUR = 4
    TEN = 10
    if ZERO < n < TEN**FIVE:
        match n:
            case i if i == FIRST or i % FIVE ==0 or i % FOUR == 0:
                return 'составным'
            case _:
                return 'простое'
    else: return 'Не соответсвие диапозону чисел'    
# print(dz(99999))

def dz_2(a,b,c):
    lis = [a,b,c]
    triangle = 'не существует' if any(i in [x+z for x in lis for z in lis[1:]] for i in lis) else 'существует'
    if triangle == 'существует':
        print([lis[i:i+1] == lis[i+1:i+2] for i,v in enumerate(lis)].count(True))
        if len(set(x==i for x in lis for i in lis[1:])) < 2:
            return f'Треугольник сюществует со сторонами {a}-{b}-{c} и являеться равносторонним'
        
        elif [lis[i:i+1] == lis[i+1:i+2] for i,v in enumerate(lis)].count(True) == 1:
            return f'Треугольник сюществует со сторонами {a}-{b}-{c} и являеться равнобедренным'
        else:
            return f'Треугольник сюществует со сторонами {a}-{b}-{c} и являеться разносторонним'
    else:
        return f'Треугольник {triangle}'

# print(dz_2(3,3,3))

from random import randint
 

def dz(n=input("Угадайте число от 0 до 1000: ")):
    LOWER_LIMIT = 0
    UPPER_LIMIT = 1000
    COUNT = 10
    num = randint(LOWER_LIMIT, UPPER_LIMIT)
    try:
        n = int(n)
        while COUNT != LOWER_LIMIT:
            if n > num:
                COUNT -=1
                print(f'Введённое число {n} больше загадонного\n'
                      f'У вас осталось {COUNT} попыток\n') 
                n = int(input("Угадайте число от 0 до 1000: "))
                
            elif n < num:
                COUNT -=1
                print(f'Введённое число {n} меньше загадонного\n'
                      f'У вас осталось {COUNT} попыток\n') 
                n = int(input("Угадайте число от 0 до 1000: "))
                
            else:
                print(f"Ты угадал число {num}")
                break
        else:
            print('Были исчерпоны все попытки')         
    except ValueError:
        print('Не верный символ\n'
              'Завершение программы\n')


dz()    