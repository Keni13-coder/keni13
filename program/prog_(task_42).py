# def zero(funk=None):
#     a = 0
#     return   eval(f'{str(a)}{funk}') if funk != None else str(a)

# def one(funk=None):
#     a=1 
#     return  eval(f'{str(a)}{funk}') if funk != None else str(a)

# def two(funk=None):
#     a=2
#     return   eval(f'{str(a)}{funk}') if funk != None else str(a)

# def three(funk=None):
#     a=3
#     return   eval(f'{str(a)}{funk}') if funk != None else str(a)

# def four(funk=None):
#     a=4 
#     return   eval(f'{str(a)}{funk}') if funk != None else str(a)

# def five(funk=None): 
#     a=5
#     return   eval(f'{str(a)}{funk}') if funk != None else str(a)

# def six(funk=None): 
#     a=6
#     return   eval(f'{str(a)}{funk}') if funk != None else str(a)

# def seven(funk=None): 
#     a=7
#     return  eval(f'{str(a)}{funk}') if funk != None else str(a)

# def eight(funk=None): 
#     a=8
#     return   eval(f'{str(a)}{funk}') if funk != None else str(a)

# def nine(funk=None): 
#     a=9
#     return   eval(f'{str(a)}{funk}') if funk != None else str(a)

# def plus(num): 
#     return f'+{(num)}'

# def minus(num): 
#     return f'-{str(num)}'

# def times(num): 
#     return f'*{str(num)}'
# def divided_funky(num): 
#     return f'//{str(num)}'

# print(seven(divided_funky(nine())))

# Вариант №2
def zero(cb=None): return cb(0) if cb else 0
def one(cb=None): return cb(1) if cb else 1
def two(cb=None): return cb(2) if cb else 2
def three(cb=None): return cb(3) if cb else 3
def four(cb=None): return cb(4) if cb else 4
def five(cb=None): return cb(5) if cb else 5
def six(cb=None): return cb(6) if cb else 6
def seven(cb=None): return cb(7) if cb else 7
def eight(cb=None): return cb(8) if cb else 8
def nine(cb=None): return cb(9) if cb else 9

def plus(n): return lambda x: x+n
def minus(n): return lambda x: x-n
def times(n): return lambda x: x*n
def divided_by(n): return lambda x: x//n

def d(func): return func(7)
# print(seven(divided_by(nine())))
seven(lambda cb: cb + n five())

b = 7
print(b(lambda x: x+6))