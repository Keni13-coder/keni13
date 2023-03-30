# Верное решение но codewars думает иначе
# def simple_multiplication(*number):
#     return [ i*8 if i % 2 ==0 else i*9 for i in number ]

# print(simple_multiplication(5))

def simple_multiplication(number):
    return number*8 if number % 2 ==0 else number*9
print(simple_multiplication(5))