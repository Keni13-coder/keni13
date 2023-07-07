def dig_pow(n, p):
    rezul = 0
    for i,x in enumerate(str(n),1):
        rezul+= int(x) ** i

    return rezul // n  if not (rezul / n) % 1 else -1 


print(dig_pow(89, 1))

def dig_pow(n, p):
    # rezul = [int(v)**i for i,v in enumerate(str(n))]
    rezul = sum(map(lambda i:int(i[1])**i[0] ,enumerate(str(n),1)))
    return rezul // n  if not (rezul / n) % 1 else -1


print(dig_pow(89, 1))