def pig_it(text):
     return " ".join([x + 'ay' if x.isalpha() else x for x in map(lambda x: f'{x[1::]}{x[0]}',text.split())])


print(pig_it("O tempora o mores !")) #'igPay atinlay siay oolcay'

    # return " ".join(map(lambda x: f'{x[1::]}{x[0]}ay',text.split()))