def order(sentence):
    index = [int(i)-1 for i in sentence if i.isdigit()==True]
    word = sentence.split()
    zipped_pairs = zip(index, word)
    return  ' '.join(list( y for x,y in sorted(zipped_pairs)))
# чтобы сортировать  по выбору используем key = lambda x: x[index],где индекс элемента кортежа
print(order("4of Fo1r pe6ople g3ood th5e the2"))

def orders(sentence):
     return " ".join([x for y,x in sorted(zip([int(i)-1 for i in sentence if i.isdigit()==True],sentence.split()))])
print(orders("4of Fo1r pe6ople g3ood th5e the2"))

def orderss(sentence):
# key = min отсортирует по минимульному числу которое найдёт, если числа нет идёт в конец   
    return " ".join(sorted(sentence.split(),key=min))
print(orderss("4of Fo1r pe6ople goo0d th5e the2"))

def ordersss(sentence):
    # хз как это работает, сортируем сортируемое
    return ' '.join(sorted(sentence.split(), key=lambda w:sorted(w)))



print(ordersss("4of Fo1r pe6ople goo0d th5e the2"))