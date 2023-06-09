import pandas as pd
import seaborn as sns
rd = pd.read_excel('C:\it is prank\Test\ddd.xlsx')
# rd.loc[rd['Вес'] == 'хз', 'Вес'] = 'No information'
# rd.to_excel('C:\it is prank\Test\ddd.xlsx')
# rr = pd.DataFrame(rd.dropna(axis=1))
'Чтобы избавиться от безымянных столбцов, вы также можете использовать регулярное выражение, такое как df.drop(df.filter(regex="Unname"),axis=1, inplace=True)'
"""rr.columns.str.match('Unnamed')
str.match -итерирует по колонкам 
columns.str.match - итерирует именя колонек
print(rr.loc[:,~rr.columns.str.match('Unnamed')])"""
# del rd['Unnamed: 6']
# rr = rd.iloc[:,4:13]
# rd = pd.DataFrame(rd.drop(rd.filter(regex="Unname"),axis=1)) 
# rd.to_excel('C:\it is prank\ddd.xlsx')
for x,y in rd.iterrows():
    print(f'index: {x} row: {y}')

# 1. Создание фрейм данных и перенос в файл
# frame = pd.DataFrame(np.arange(16).reshape((4,4)),
# 		 index = ['red', 'blue', 'yellow', 'white'],
# 		 columns = ['ball', 'pen', 'pencil', 'paper'])
# frame.to_csv('ch05_07.csv')

# fr = pd.read_csv('C:\it is prank\ch05_07.csv',index_col=0)
# print(fr)

# print(sns.scatterplot(data=fr, x='pen',y='paper'))
'''
2. Создание фрейма и поиск по нему 
# data = {
#     'apples': [3, 2, 0, 1], 
#     'oranges': [0, 3, 7, 2]
# }
# purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])
# print(purchases.loc['June'])'''


