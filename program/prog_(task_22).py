def row_sum_odd_numbers(n):
    # sum = 0
    # start = (n * n) - (n - 1)
    # end = start + n * 2
    # for i in range(start, end, 2):
    #     sum += i
    # return sum
    return  n ** 3  
print(row_sum_odd_numbers(17)) 

# ебать я тупень

# фибаначи
    # f1 = f2 = 1
    # for i in range(2, n):
    #     f1, f2 = f2, f1 + f2
    # return f2