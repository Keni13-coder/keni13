# def summation(num):
#     f = 1
#     while num > 1:
#         f += num
#         num -= 1
#     return f    

# print(summation(8))

# def summation(num):
#     f = 0
#     for i in range(num+1):
#         f +=i 
#     return f    
# print(summation(100))


def summation(num):
    return sum(range(num + 1))

print(summation(8))