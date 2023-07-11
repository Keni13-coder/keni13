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
scv.reader(file) - построчное чтение файла, строка являеться list 
scv.reader(file, dialect=excel-tab)-  в обычной чтение читаеться через зяпятую, через dialect=excel-tab мы говорим что разделитель TAB
scv.reader(file, quoting = cvs.QUOTE_NONNUMERIC) - если число не было в кавчках, то преобразует в число
'''