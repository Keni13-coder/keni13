def alphabet_position(text):
    d ={ "a":1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
    return ' '.join((map(str,[d.get(x) for x in text.replace(' ', '').lower() if d.get(x) != None])))
print(alphabet_position("The sunset sets at twelve o' clock."))


def alphabet_positions(text):
    # ord принемает в себя строчный символ и переводит в число Юникода, алфовит начинаеться с 97 позиции
    # c.isalpha() делает проверку на буквиость
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
print(alphabet_positions("The sunset sets at twelve o' clock."))
