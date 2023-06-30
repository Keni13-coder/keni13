def sum_dig_pow(a, b): 
    return [x for x in range(a,b+1) if sum(int(v)**i for i,v in enumerate(str(x),1))==x]



print(sum_dig_pow(90,100))
