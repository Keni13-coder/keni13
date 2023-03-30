def count_sheeps(sheep):
    result = 0
    return sum([result+1  for i in sheep if i ==True])

print(count_sheeps([True,  True,  True,  False,
True,  True,  True,  True ,
True,  False, True,  False,
True,  False, False, True ,
True,  True,  True,  True ,
False, False, True,  True ]))


array = [True,  True,  True,  False,
True,  True,  True,  True ,
True,  False, True,  False,
True,  False, False, True ,
True,  True,  True,  True ,
False, False, True,  True ]

array = array.count(True)
print(array)