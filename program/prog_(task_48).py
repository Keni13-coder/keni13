
# def fib(n):
#     if n == 0:
#         return 0
#     return 1 if n in (1,2) else fib(n-1) + fib(n-2)

def productFib(prod):
    fib1,fib2 =0, 1
    if prod == 0:
        return [fib1,fib2, True]
    for x in range(prod):
        fib1,fib2 = fib2, fib1 + fib2
        if fib1 * fib2 == prod:
            return [fib1, fib2, True]
        elif fib1 * fib2 > prod:
            return [fib1, fib2, False]
        
def productFib(prod):
  a, b = 0, 1
  while prod > a * b:
    a, b = b, a + b
  return [a, b, prod == a * b]        

print(productFib(4895))

print(89 * 144)