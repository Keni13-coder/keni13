# with open('C:\it is prank\keni13\Lesson_python\lesson_second\lesson\\text.txt',encoding='utf-8') as f:
#     # print(f)
#     print(' '.join(f).split('\n'))
'r - для чтения'
"w - окрыть файл для записи, перд этим очистив файл, если файла нет создаёт"
'x - открыть для создание файла, усли файл уже есть вызывает ошибку'
'a - открыть для записи в конец файла, если он существует и создаёт и записывает в начало если не существует'
'b -  запись в бинарном режиме'
'+ - чтение запись'
" открытие нескольких файлов with (open,open,open): "
'чтение файла - list(f), f.read(), f.readline(), for line in f'
'файл - читаеться 1 раз , если в read передать int то будет считывать по int символов '
"строки возвращаються с окочанием \n"
# with open('C:\it is prank\keni13\Lesson_python\lesson_second\lesson\\text.txt',encoding='utf-8') as f:
#      readlines возвращает список строк принцип разделение на элементы списка конец строки \n
#      read возвращает строку
#     r = f.readline()
#     d = f.read()
#     print(r)
#     print('Это d',d)
'запись производиться путём write, writeline, print("чт0-то",file=f)'
'метод write - возвращает количество записанных символов'
'write - добовляет 1 строку'
'writelines - итерирует список и добовляет в файл, конструкция "\n".join(text) позволяет добоалять строки с переносом'
# text = ['''Dicta impedit quia quibusdam excepturi, quis quasi, porro incidunt sunt, asperiores veritatis blanditiis vitae esse placeat! Nam placeat accusantium assumenda?
#             Voluptatum earum quam atque. Nulla ipsa alias quidem natus quia.''',
#         '''Rerum odio perferendis rem ipsam dolorem harum libero nihil at, molestias expedita? Odit fugit beatae pariatur 
#             laborum omnis non odio debitis asperiores fugiat, magnam in minima iure quos earum consectetur?''',
#         '''Non deleniti quidem nesciunt cum ipsum doloribus corporis sunt labore culpa illum dicta, ipsa repellat blanditiis beatae.
#             Nihil, repellat, vel quam consequuntur non deserunt officia molestiae laborum nesciunt, eius similique?''']
# with open('C:\it is prank\keni13\Lesson_python\lesson_second\lesson\\text.txt','a',encoding='utf-8') as f:
#     f.writelines('\n'.join(text))
'print("чт0-то",file=f) - идёт добовление с переносом тк print обладает end=\n '
'print("чт0-то",file=f) - добовляет 1 строку, конструкия print("чт0-то", end="***\n###" ,file=f) позволяет понимать где начало строки, а где конец, символы могут быть любые '

'f.tell - возвращает целое число int, текущая позиция указателя.'
'''f.seek(offset[, whence]) - возвращает целое число int, новая позиция указателя. меняет позицию указателя записи, например, последнияя запись 208 символ,
слдующая запись будет начиная с 208, f.seek(134,0) - теперь запись пойдёт с 134 символа от начала файла, 0 говорит о том что мы отсчитываем от начального укзателя,
если с начала 134 были строки, они будут заменены'''


'                                                          2 часть                                         '
'("../.. ") - являеться указателем на представление записи дерикторий'
''' 
    os
    os - os.getcwd() - получить текущую дерикторию
    os.chdir("../.. ")- изменить дерикторию
    os.mkdir("../.. ") - создать дерикторию
    os.mkdirs("../.. ") - создать вложенную дерикторию
    если дериктория уже есть выдаёт ошибку
    os.rmdir("../.. ") - удалить дерикторию
    если дериктория не пуста, например в папке что-то есть, выдаёт ошибку
    os.path.join(путь_1 , * путь) - нужна для правельного составлений дерикторий, берёт путь_1 и совмещает с *путями
    os.listdir() - показывывает что есть в текущей дериктории, файлы каталоки папки, в листе 
    os.path.isdir(obj) - проверяет является ли дерикторией
    os.path.isfile(obj) - проверяет является ли  файлом
    os.path.islink(obj) - проверяет является ли  ссылкой
    os.walk() - рекурсивно проходит каждую папку указанной дериктории и показывает что в них, если в папках другие папки заходит и в них
    os.rename() - переименовать
    os.replace(old_name, os.join(os.getcwd(), dir, new_name) - replace перемещает файлы, с помощью join мы составляем предсатвление дериктории и указываем новое имя
    os.remove() - удаляет файлы
'''
'''
    pathlib - Path, 
    Path().cwd() - получить текущую дерикторию
    Path().mkdir("../.. ") - создать дерикторию
    Path().mkdir(parents=True) - создать вложенную дерикторию
    если дериктория уже есть выдаёт ошибку
    Path().rmdir("../.. ") - удалить дерикторию
    если дериктория не пуста, например в папке что-то есть, выдаёт ошибку
    Path().cwd() / следующий каталог / файл - создаёт праильный путь к файлу и обрабатывает в зависимости от операционной системы
    p = Path(Path().cwd())
    for obj in p.iterdir():
        print(obj)
    - Выводит все существуещии дериктории, начаная с текущий рабочая область смотрит что есть в каждой, папке в каждом каталоге.
        p = Path(Path().cwd())
    for obj in p.iterdir():
        print(f"{obj.is_dir()}") - проверяет является ли дерикторией
        print(f"{obj.is_file()}") - проверяет является ли  файлом
        print(f"{obj.is_symlink()}") - проверяет является ли  ссылкой
        Path().rename() - переименовать 
    old_file = Path(old_name)
    new_file = old_file.replace(Path().cwd() / folder / old_file)
    такая конструкция перемещает в ново - созданное  предсатвление дериктории с помощью (Path().cwd() / folder  / old_file)
    Path().unlink() - удаляет файлы
'''

'''
    shutil
    shutil.rmtree("../.. ") - удяляет все содержимое до указанного
    shutil.copy(name, name_copy) - создаёт копию файла, если имя одинаковые будет замена
    shutil.copytree(name, name_copy) - копируется всё, если папки вложенные
    shutil.rmtree(name) - удаляет всю name
'''