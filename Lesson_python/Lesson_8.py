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
def show_menu():
    print("\nВыберите необходимое действие:\n"
          "0. Создать справочник\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Закончить работу")
    choice = int(input('Введите номер действия: '))
    
    return choice


def zero():
    name = input("Введите название файла: ")
    with open(f'{name}.txt','w+',encoding='utf=8') as f:
        f.write('Мой справочник:\n')
        return f


def funk_1(name: str):
    with open(name,'r',encoding='utf=8') as n:
        [print(x,end='') for x in n ] 

# funk_1('file.txt')
# show_menu()
def funk_2(name: str):
    cursor = input('Введите фамилию: ')
    with open(name,'r+',encoding='utf=8') as f:
        [ print(x[:-1]) if  '\n' in x else print(x) for x in f if cursor.casefold() in x.casefold()]
    
# funk_2('file.txt')

def funk_3(name: str):
    cursor = input('Введите телефон: ')
    with open(name,'r+',encoding='utf=8') as f:
        [ print(x[:-1]) if  '\n' in x else print(x) for x in f if cursor.casefold() in x.casefold()]

# funk_3('file.txt')


def funk_4(name: str):
    with open(name,'a+',encoding='utf=8') as f:
        
        first_name = input('Введите Имя: ')
        second_name = input('Введите Фамилию: ')
        three_name = input('Введите Отчество: ')
        number_name = input('Введите номер: ')
        ls = [first_name,second_name,three_name,number_name] 
        [f.write(f'{x}\n') if x == number_name else f.write(f'{x}, ') for x in ls]
        print('Запись добавлена')

# zero()
funk_4('file.txt')