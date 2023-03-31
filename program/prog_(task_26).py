def friend(x):
    # return[i for i in x if len(i)==4]
    
    return list(filter(lambda name: len(name) == 4, x))
# Лучше привыкать такому типу задать через filter
print(friend(["Ryan", "Kieran", "Mark",]))