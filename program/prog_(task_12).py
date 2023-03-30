# def basic_op(operator, value1, value2):
#     dicti={
#         "+": value1 + value2,
#         "-": value1 - value2,
#         '*': value1 * value2,
#         "/": value1 / value2
#     }
#     return dicti[operator]
# print(basic_op('+', 4, 7))

def basic_op(operator, value1, value2):
    return eval('{}{}{}'.format(value1, operator, value2))


print(basic_op('+', 4, 7))

a,b,c ="am","+","asdsa"

print(eval("{}{}{}".format(a,b,c)))