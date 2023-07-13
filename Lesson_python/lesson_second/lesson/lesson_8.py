''' json.load(file) - из json файла получить объект пайтона,читает и преобразовывает
    json.loads(json_text) - преобразовывает текстовое представление json в объект питона
    json.dump(dict,file) - сохранение обекта питона в json file
    json.dumps() - сохранение обекта питона в json строку
    json.dump(ensure_ascii=False) - для отключение аске, чтоб бывол видно другие языки
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
import csv

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

def task_2()-> None:
    while True:
        end = input('Для выхода введите exit или enter чтобы продолжить: ')
        if 'exit' == end:
            break
        name = input('Введите имя: ')
        id_ = input('Введите id: ')
        level = input('Введите уровень доступа: ')

        with open('Lesson_python\lesson_second\lesson\\test.json','r+',encoding='utf-8') as f:
            try:
                read_ : dict = json.load(f)
                vulues = [x for x in read_.values()]
            except json.decoder.JSONDecodeError:
                vulues = []
                read_ = {}
            if level not in read_:
                if not any(map(lambda x: id_ in x , vulues)):
                    read_[level] = {id_:name}
                
            else:
                if not any(map(lambda x: id_ in x , vulues)):        
                    read_.setdefault(level,{}).update({id_:name})
                
            with open('Lesson_python\lesson_second\lesson\\test.json','w+',encoding='utf-8') as rezul:
                json.dump(read_,rezul,ensure_ascii=False,indent=2,sort_keys=True)
                
                
                
                
'''
Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV.
'''
def task_3()-> None:
    with open('Lesson_python\lesson_second\lesson\\test.json','r',encoding='utf-8') as f:
        reader_ : dict= json.load(f)
        print(reader_)
        with open('Lesson_python\lesson_second\lesson\\testing.csv','w',encoding='utf-8',newline='') as rez:
            writer = csv.DictWriter(rez,fieldnames=[*reader_.keys()])
            writer.writeheader()
            writer.writerow(reader_)






'''
Задание №4
Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка
csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы
функции.
'''


def task_4()->None:
    with open('Lesson_python\lesson_second\lesson\\testing.csv','r',newline='',encoding='utf-8') as file:
        reader = [*csv.reader(file)]
        rez = {x: y for (x,y) in [*zip(reader[0],reader[1])]}
        # rez = json.dumps(rez,ensure_ascii=False)
        # rez = json.loads(rez)
        for k,v in rez.items():
            v = json.loads(v.replace("'",'"'))
            for x in v.values():
                print(x)
    


if __name__ == '__main__':
    # task_1('rezul.txt')
    # task_2()        
    # task_3()
    task_4()