def stock_list(list_of_art, list_of_cat):
    d = {}
    for x in list_of_cat:
        for v in list_of_art:
            if x == v[0]:
                d.setdefault(x,[]).append(int(v.split()[1]))
            else:
                d.setdefault(x,[]).append(0)    
    return ' - '.join([f'({x} : {sum(v)})' for x,v in d.items()])
    # for x in list_of_art:
    #     num = x.split()[1]
    #     el = x[0]
    #     d.setdefault(el,[]).append(num)
    # return d    

a = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]

b = ["A", "B", "C", "D"]
d = {1:0}
# print(stock_list(a,b))


from collections import defaultdict
from typing import List


def stock_list(list_of_art: List[str], list_of_cat: List[str]) -> str:
    if not list_of_art or not list_of_cat:
        return ""
    cats = defaultdict(int)
    # defaultdict создаёт словарь со значениеми инт
    # рабоатает так же как и setdefault, смотрит на ключ и добавляет значение, если ключа нет создаёт его, но действует быстрей
    for a in list_of_art:
        # создаёт ключть со значениями, добовляя если ключь уже существует
        cats[a[0]] += int(a.split()[1])
    print(cats['A'])
    # В отличии от простого словоря defaultdict не вызовит ошибку если ключа нет,покажет тип значения, например для int это 0, для list []
    return ' - '.join(f"({c} : {cats[c]})" for c in list_of_cat)


print(stock_list(a,b))
d = defaultdict(list)
for _ in range(5):
    d[1] += [1]
    
print(d[2])
