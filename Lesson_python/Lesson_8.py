import shutil
'''
Задача №49. Решение в группах
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
фамилия имя очество телефон

def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Закончить работу")
    choice = int(input())
    return choice
'''
'''
try:
        with open('file.txt','r+',encoding='utf=8') as f:
            f.write("член")

    except  Exception :
        with open('file.txt','w+',encoding='utf=8') as f:
            f.write("хуй")


'''
name = None
def start():
    global name
    name = input('Введите имя файла для работы справочника: ')
    if name == 'exit':
        pass
    return name
def show_menu():
    print("\nВыберите необходимое действие:\n"
          "0. Создать справочник\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Клонировать справочник в текстовом формате\n"
          "6. Закончить работу")
    choice = int(input('Введите номер действия: ').strip())

    while choice > 6:
        print('Введенный номер не соответствует командам!!!')
        print("\nВыберите необходимое действие:\n"
          "0. Создать справочник\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Удалить абонента\n"
          "7. Изменение данных\n")
        choice = int(input('Введите номер действия: ').strip())
    return choice


def zero():

    with open(f'{name}.txt','w+',encoding='utf=8') as f:
        f.write('Мой справочник:\n')
        print(f' Файл и именем {name}.txt успешно создан !')



def funk_1():
    with open(f'{name}.txt','r',encoding='utf=8') as n:
        [print(x,end='') for x in n ]


# funk_1('file.txt')
# show_menu()
def funk_2():
    cursor = input('Введите фамилию: ').strip()
    with open(f'{name}.txt','r+',encoding='utf=8') as f:
        [ print(x[:-1]) if  '\n' in x else print(x) for x in f if cursor.casefold() in x.casefold()]

    
# funk_2('file.txt')

def funk_3():
    cursor = input('Введите телефон: ').strip()
    with open(f'{name}.txt','r+',encoding='utf=8') as f:
        [ print(x[:-1]) if  '\n' in x else print(x) for x in f if cursor.casefold() in x.casefold()]


# funk_3('file.txt')


def funk_4():
    with open(f'{name}.txt','a+',encoding='utf=8') as f:
        
        first_name = input('Введите Имя: ').strip()
        second_name = input('Введите Фамилию: ').strip()
        three_name = input('Введите Отчество: ').strip()
        number_name = input('Введите номер: ').strip()
        ls = [first_name,second_name,three_name,number_name] 
        [f.write(f'{x}\n') if x == number_name else f.write(f'{x}, ') for x in ls]
        print('Запись добавлена')
        
def funk_5():
    second_name = input('Введите имя файла клона: ')
    with open(f'{second_name}.txt','w+',encoding='utf=8') as f: 
       return shutil.copy(f'{name}.txt',f'{second_name}.txt')
    

def funk_6():
    one_flag = input('Введите имя абонента: ').strip()
    two_flag = input('Введите фамилию абонента: ').strip()
    with open(f'{name}.txt','r+',encoding='utf=8') as f:
       d = f.readlines()
    with open(f'{name}.txt','w+',encoding='utf=8') as f:   
        for number,line in enumerate(d):
            if one_flag not in line and two_flag not in line:
                f.write(line)



def all_functional(int):
    if int == 0:
        return zero()
    elif int == 1:
        return funk_1()
    elif int == 2:
        return funk_2()
    elif int == 3:
        return funk_3()    
    elif int == 4 :
        return funk_4()
    elif int == 5 :
        return funk_5()


def main():
    print('Приветствую вас в программе "Так себе код"')
    start()
    sh = 0
    while sh < 8:
        sh = show_menu()
        all_functional(sh)

    print('Завершение программы.')



# try:
#     main()

# except Exception as ex:
#     while ex:
#         print(f'{ex}')
#         main()        
start()
# zero()
funk_6()
