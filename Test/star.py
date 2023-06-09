'''
ряды звёзд по N
'''

def test(N):
    return [print('_' * (N//3*3-i) + '*' * (i+i+1)+ '_' * (N//3*3-i)) if i % 2 != 0 else print('_' * (N//3*3-i) + 'o' * (i+i+1)+ '_' * (N//3*3-i))  for i in range(N)]

test(10)