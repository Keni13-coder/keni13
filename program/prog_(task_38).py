def duplicate_encode(word):
    return"".join(['(' if word.lower().count(x) == 1 else ')' for x in word.lower()])


print(duplicate_encode("kXKO)xU CBpafUhAsY)e@ e)MyVOkMNy z!Vj"))