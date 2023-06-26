def rot13(message):
    lis = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join([lis[lis.index(x)-13] if x in lis else lis[lis.index(x.lower())-13].upper() if x.lower() in lis else x for x in message])

print(rot13('aA bB zZ 1234 *!?%'))