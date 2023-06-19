def is_pangram(s):   
    srs = 'abcdefghijklmnopqrstuvwxyz'
    return True if len({x for x in s.casefold() if x in srs}) >= len(srs) else False

st = "The quick, brown fox jumps over the lazy dog!"

print(is_pangram(st))
def is_pangram(s):
    return True if set('abcdefghijklmnopqrstuvwxyz').issubset(set(s.lower())) else False
    'sets.issubset(other) позволяет проверить находится ли каждый элемент множества sets в последовательности other.'