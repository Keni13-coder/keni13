from functools import reduce
def square_digits(num):
    return int( "".join( map(str,(map(lambda x:x**2,[int(i) for i in '{}'.format(num)])))))

print(square_digits(124124124))

# join применяется к стрончым объектам даже если они в list

# return int(''.join(str(int(d)**2) for d in str(num)))

# Не получилось для общего случая
