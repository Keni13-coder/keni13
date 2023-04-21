def number(lines):
    return [f'{x}: {y}' for x,y in enumerate(lines, start=1)]



print(number(["a", "b", "c"]))