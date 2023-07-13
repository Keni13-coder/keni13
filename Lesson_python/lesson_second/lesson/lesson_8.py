''' json.load(file) - из json файла получить объект пайтона,читает и преобразовывает
    json.loads(json_text) - преобразовывает текстовое представление json в объект питона
    json.dump(dict,file) - сохранение обекта питона в json file
    json.dumps() - сохранение обекта питона в json строку
    json.dump(ensure_ascill=False) - для отключение аске, чтоб бывол видно другие языки
    json.dump( indent - отвечает за переносы строк,
                separators - 2 параментра: символ между элементами и символ между ключём и значением
                sort_keys = True сортирует ключи, даже вложенные
'''
# import json
# a = 'Hello word'
# b = {key: value for key, value in enumerate(a)}
# c = json.dumps(b,indent=5,separators=(';','= '))
# print(c)

'''
wiht open(newline='')-для правельного чтения csv
csv.reader(file) - построчное чтение файла, строка являеться list 
csv.reader(file, dialect=excel-tab)-  в обычной чтение читаеться через зяпятую, через dialect=excel-tab мы говорим что разделитель TAB
csv.reader(file, quoting = cvs.QUOTE_NONNUMERIC) - если число не было в кавчках, то преобразует в число

csv.writer(f) - обычная запись в файл
csv.writer.writerow(line) - сохранение списка в одной строке
csv.writer.writerows(all_data) - сохранение матрицы в нескольких строках
csv.writer(f, delimiter=) как разделять объекты меж собой (разделение столбцов)
csv.writer(f, quotechar=|) - если символы разделители уже есть, то они будут | (символ, использующийся для "склейки" поля, содержащего специальные символы,
такие как delimiter)
csv.DictReader(f,fieldanme=[],restkey=" ", restval =" ")-читает dict 
fieldanme- список загаловков столбцов, ключей словоря
restkey=" " - имя ключа для столбца которых нет в fieldanme
restval =" " - значение ключей fieldanme который нет в csv, если колонка есть а значений нет
csv.writer.writeheader() - сохранение первой строки с заговловками
csv.writer.writerow(line)
csv.writer.writerows(all_data)
'''


'''
Piclke
сериалезуем только то в чём уверены, может быть код консольный, будут проблемы
pickle.dump(my_dict,f)  - сохранение в бинарном файле
pickle.dumps(my_dict) - сохранение в бинарную строку
pickle.dumps(, protocol) - сериализация и десериализация может быть только с одинаковыми протоколами
                   Десериализация
pickle.load(f) - загрузка из бинарного файла в объект
pickle.loads(data) - получение объекта из бинарной строки
при сериализация и десериализация объектов на уровне модуля , объекты должны быть и там и там, иначе Pickle не поймет откуда взят файл
по факту он передёт имена функции или класса и если в файле будет такое же имя, Pickle подумает что это она и есть
'''

import json


'''
Задание №1
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
'''

def task_1(file_name: str)-> None:
    with (open(file_name,'r',encoding='utf-8') as f,
          open('test_js.json','w+',encoding='utf-8') as js):
        d = dict(x.replace('\n', '').capitalize().split(':')  for x in f)
        json.dump(d,js,indent=2,separators=(', ',':'))

        
    
    
'''
Задание №2
Напишите функцию, которая в бесконечном цикле
запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в
JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо
от уровня доступа.
При перезапуске функции уже записанные в файл данные
должны сохраняться.

'''

def task_2():
    # while True:
        
    #     print('Для выхода введите exit: ')
    #     name = input('Введите имя: ')
    #     id_ = input('Введите id: ')
    #     level = input('Введите уровень доступа: ')
    #     if 'exit' in (name,id_,level):
    #         break
    #     dict_ = {id_ : {name : level}}
    #     print(dict_)
    di = {
    "Aeoupw":"833891.7", 
    "Alnqaqz":"442210", 
    "Aivdpi":"542147", 
    "Awmvea":"95904.0", 
    "Iofxws":"81015.48"
        }
    with open('Lesson_python\lesson_second\lesson\\test.json','r+',encoding='utf-8') as f:
        json.dump(di,f)

        
if __name__ == '__main__':
    # task_1('rezul.txt')
    task_2()        