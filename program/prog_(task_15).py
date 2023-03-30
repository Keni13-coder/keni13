from math import sqrt as sq
from pranks_images import men
# sqrt Находит корень
def is_square(n = input("Enter number: ")):
    n = int(n)
    print(men[2])    
    return True if n == 0 else False if n <= 0 or n % sq(n) != 0 else True

# print(is_square(-1))

# def is_squares(n):  
#     print(men[2])  
#     return n >= 0 and (n**0.5) % 1 == 0
# print(f'{is_squares(25)}{men[2]}')

# print(is_square())