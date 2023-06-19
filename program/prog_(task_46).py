def is_valid_walk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')

array = ['e', 'w', 'n', 'w', 'n', 's', 'n', 's', 'e', 'w'] # False
['e', 'w', 'n', 'w', 'n', 's', 'n', 's', 'e', 'w']

print(is_valid_walk(array))
print(array.count == 10)


'''
North [nɔːθ] — прямо
South [saʊθ] — назад
East [iːst] — право
West [west] – лево
'''
'''
->
<-
|
<-
|
'''
n = 1
s = -1
e = 1
w = -1


def ss(array):
    d = {'n' : 1,
         's' : -1,
         'e' : 2,
         'w' : -2}
    return  sum(d[x] for x in array) == 0

print(ss(['e', 'w', 'n', 'w', 'n', 's', 'n', 's', 'e', 'w'] ))


