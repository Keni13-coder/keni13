from random import randint
def dz_3(n=input("Угадайте число от 0 до 1000: ")):
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
            print(f'Были исчерпоны все попытки\n'
                  f'задуманно было число {num}\n')         
    except ValueError:
        print('Не верный символ\n'
              'Завершение программы\n')


dz_3()