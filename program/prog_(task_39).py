def series_sum(n):
    i = 1
    z = 4
    suma = 1
    if n > 1:
        while i < n:
            suma += 1/z
            z += 3
            i += 1
    else:
        return f'{n}.00'       
    return "{:.2f}".format(suma)
# [x for x in range(1,n)]
print(series_sum(59))

def series_sums(n):
    # return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
    return f"{sum(1 / i for i in range(1, (n * 3) + 1, 3)): .2f}"

print(series_sums(59))
