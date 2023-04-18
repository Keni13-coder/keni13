def likes(names):
    return 'no one likes this' if len(names) == 0 else f'{names[0]} likes this' if len(names) ==1 else f"{' , '.join([x for x in names])} like this".replace(',', 'and') if len(names) == 2 else f"{' , '.join([x for x in names])} like this".replace(',', 'and').replace(' and', ",",1) if len(names) <= 3 else f'{names[0]}, {names[1]} and {len(names)-2} others like this'


print(likes(['Alex']))



def likess(names):
    d = {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this"
        }
    length = len(names)
    return d[min(4, length)].format(*names, others = length - 2)

