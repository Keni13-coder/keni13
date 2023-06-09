import pandas as pd
import seaborn as sns
rd = pd.read_excel('C:\it is prank\ddd.xlsx',skiprows=[0],nrows=5,header=None)
'''
# print(rd)

# 1. Создание фрейм данных и перенос в файл
# frame = pd.DataFrame(np.arange(16).reshape((4,4)),
# 		 index = ['red', 'blue', 'yellow', 'white'],
# 		 columns = ['ball', 'pen', 'pencil', 'paper'])
# frame.to_csv('ch05_07.csv')

fr = pd.read_csv('C:\it is prank\ch05_07.csv',index_col=0)
print(fr)'''

'''Создание фрейма и поиск по нему 
# data = {
#     'apples': [3, 2, 0, 1], 
#     'oranges': [0, 3, 7, 2]
# }
# purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])
# print(purchases.loc['June'])'''

'''
Методы pandas
read - читает таблицу
head - показывает стоки таблицы с начала
tail - показывает строки таблицы с конца
info - показывает основную информацию о количестве и типе
shape - Он выводит просто кортеж (строки, столбцы)
append - вернет копию, не затрагивая исходный DataFrame.
drop_duplicates - вернет копию, без дубликатов
inplace= True изменит исходный объект DataFrame
columns - выводит наименование колонок
rename - для переименования определенных или всех столбцов с помощью словаря.
    rename(columns={})
поменять регистор в columns через чикл
    columns = [col.lower() for col in columns] 
isnull - возвращает DataFrame, в котором каждая ячейка либо True, либо False
sum - итерирует колонки 
dropna - Эта операция удалит любую строку, содержащую хотя бы одно нулевое значение, но вернет новый DataFrame без изменения исходного.
    чтобы изменить исходный  используем аргумент inplace= True   
dropna(axis=1) - вы также можете отбросить столбцы с нулевыми значениями
fillna - меняет значение null на что-то fillna(null, new_num)
describe - мы можем получить сводку распределения непрерывных переменных , а именно  
        количество строк, количество уникальных категорий, топовую категорию и ее частоту
        
value_counts -  позволяет определить частотность всех значений в столбце           
'''