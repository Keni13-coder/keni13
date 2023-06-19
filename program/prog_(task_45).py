def wave(people):
    return [''.join([people[i].upper() if i == z else x for z, x in enumerate(people)]) for i,v in enumerate(people) if v != ' ']


print(wave('two words'))
['Two words', 'tWo words', 'twO words', 'two words', 'two Words', 'two wOrds', 'two woRds', 'two worDs', 'two wordS']
['Two words', 'tWo words', 'twO words', 'two Words', 'two wOrds', 'two woRds', 'two worDs', 'two wordS']