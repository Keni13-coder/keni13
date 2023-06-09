def funk(a,b):
    if b == 0:
        return [b]
    return [a] + funk(a+b,b-1)
'''
2 , 5
7 , 4
11 , 3
14 , 2
16, 1
17, 0 return 0
[0]
[16] + [0]
[16,0]
[14] + [16,0]
[14,16,0]
[11] + [14,16,0]
[11,14,16,0]
[7] + [11,14,16,0]
[7,11,14,16,0]
[2] + [7,11,14,16,0]
return [2,7,11,14,16,0]
'''


# print(funk(2,5))


'''
Распаковка вложенных списков 

'''
array = [[[3]],[[4,5]],[[6,7]]]
# print(sum(array,[]))
# print(sum(array,[]) if all(isinstance(x,list) for x in array) else 'Список не коректный')


# 1.
def reck(arr):
    new_array = array[:]
    ind = 0
    while True:
        try:
            while isinstance(new_array[ind], list):
                item = new_array.pop(ind)
                print(item)
                for inner_item in reversed(item):
                    new_array.insert(ind, inner_item)
            ind += 1
        except IndexError:
            break
    return new_array

# print(reck(array))


# 2.

def tishka_flatten(data: list) -> list:
    """
    Non recursive algorithm
    Based on append/extend elements to new list

    """
    nested = True
    while nested:
        new = []
        nested = False
        for i in data:
            if isinstance(i, list):
                new.extend(i)
                nested = True
            else:
                new.append(i)
        data = new
    return data


# 3.
def zart_flatten(a: list) -> list:
    """
    Non recursive algorithm
    Based on pop from old and append elements to new list
    """
    queue, out = [a], []
    while queue:
        elem = queue.pop(-1)
        if isinstance(elem, list):
            queue.extend(elem)
        else:
            out.append(elem)
    return out[::-1]

# print(zart_flatten(array))

def recursive_flatten_iterator(arr: list) -> list:
    """
    Recursive algorithm based on iterator
    Usual solution to this problem
    """

    for i in arr:
        print(i)
        if isinstance(i, list):
            print(f' в рекурсии {i}')
            yield from recursive_flatten_iterator(i)
        else:
            yield i

print([x for x in recursive_flatten_iterator(array)])



def ttt():
    gen_1 = (x for x in range(5))
    gen_2 = (x for x in range(10))
    yield from gen_1
    yield from gen_2
    
    
gen = ttt()   

# print([x for x in gen]) 
    
    