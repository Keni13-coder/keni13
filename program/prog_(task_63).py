def increment_string(strng):
    start_ = [x for x in strng][::-1]
    rez = []
    index = []
    for i,v in enumerate(start_):
        if v.isdigit():
            # rez.append(start_.pop(i))
            index.append(i)
            rez += v
        else:
            break
    for _ in index:
        print(start_[::-1].pop())
      
    for i,x in enumerate(rez):
        if x == '9':
          rez[i] = '0'
        else:
            rez[i] = str(int(x)+1)
            break    
        
    return ''.join(start_),rez
a = "fo99obar99"
# print(increment_string("foobar0001"))
'сделать список из строки и поменять срез со цыфрами '
a = "foobar001"
b =[a[-i:] for i,x in enumerate(a,1) if a[-i:].isdigit()][-1]
# b =[*map(int,b)]
# b[-1] +=1
# b =[*map(str,b )]
a = [x for x in a]
a[-1:-len(b)-1:-1] = b[::-1]
print()


# f'{strng[:-1] + str(int(strng[-1])+1)}' if strng[-1].isdigit() else strng + '1'
# for x in a:
#     if x.isdigit() and a.endswith(x):
#         print(x)



'''    num = str(eval(f"{''.join([x for x in strng if x.isdigit()])}+1"))
    strng = ''.join([x for x in strng if x.isalpha()]) 
    return strng + num if num else strng + '1' '''
    
'''
        for i,v in enumerate(strng):
        if strng[i:].isdigit():
            print(strng[i:])
    
'''

'''
    try:
        num = str(eval(f'{[strng[i:] for i,v in enumerate(strng) if strng[i:].isdigit()][0]}+1'))
    except SyntaxError:
        num = str(eval(f'{[strng[i:] for i,v in enumerate(strng) if strng[i:].isdigit()][1]}+1'))
    return num

'''

'''
    rez = ''
    start = ''
    for i,v in enumerate(strng[::-1]):
        if v.isdigit():
            rez += v
        else:
            start += v
    try:
        rez = str(int(rez[::-1])+1)
    except SyntaxError:
        rez = str(int(rez[::-1].split(0)[1])+1)    
    return  start[::-1]+rez 


'''

'''
    rez = ''
    start_ = ''
    for i,x in enumerate(strng,1):
        if strng[-i].isdigit():
            if strng[-i]=='9':
                rez += '0'
            else :
                continue
        else:
            start_ += strng[-i]
    if len(set(rez)) <2 and rez:
        rez = '1'+ rez[::-1]
    else:
        rez = str(int(strng[-1])+1)
        return strng[:-1]+rez        
    return start_[::-1] + rez  
'''