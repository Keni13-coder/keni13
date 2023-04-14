from string import capwords
def to_jaden_case(string):
    return capwords(string) 
quote = "How can mirrors be real if our eyes aren't real"
print(to_jaden_case(quote))

# Так работает capwords
def to_jaden_cases(string):
    return ' '.join(word.capitalize() for word in string.split()) 

print(to_jaden_cases(quote))