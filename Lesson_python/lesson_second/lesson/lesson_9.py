'множественные дикораторы работают по принципу стека - снизу вверх запоминает и также сначала происходит возвращение основной функции, с вверху вниз закрывает'
import random
from typing import Callable
def cache(func: Callable):
    _cache_dict = {}
    def wrapper(*args):
        if args not in _cache_dict:
            _cache_dict[args] = func(*args)
            print(_cache_dict)
        return _cache_dict[args]
    print('Конец') # сначала возвращает конец потом wrapper
    return wrapper #  в ствою очередь wrapper возвращает  словарь с ключём (1,10)
@cache
def rnd(a: int, b: int) -> int:
    print('Запуск')
    return random.randint(a, b)


# print(f'{rnd(1, 10) = }')
# print(f'{rnd(1, 10) = }')
# print(f'{rnd(1, 9) = }')





"Декаратор с параметрами"
def count(num: int = 1):
    def deco(func: Callable):
        counter = []
        def wrapper(*args, **kwargs):
            for _ in range(num):
                result = func(*args, **kwargs)
                counter.append(result)
            return counter
        return wrapper
    return deco
@count(10) # -> параметр 10, каждый раз при вызове функции будет добовляеться 10 значений
def rnd(a: int, b: int) -> int:
    return random.randint(a, b)


print(f'{rnd(1, 10) = }')
print(f'{rnd(1, 100) = }')
print(f'{rnd(1, 1000) = }')

' decorater wraps(funk) -  из fanctools  позволяет получть информацию о функции а не о wrappers'
'decorater cache - из fanctools  позволяет получть данный которые были уже использованы не вызывая функцию, пример работы 1 задача'