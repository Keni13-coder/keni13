def lovefunc( flower1, flower2 ):
    return False if flower1 % 2 !=0 and flower2 % 2 !=0 else (flower1 % 2 !=0 or flower2 % 2 !=0) 
print(lovefunc(253,776))

