def unique_in_order(sequence):
    lis = []
    for i,v in enumerate(sequence):
        if sequence[i:i+1] == sequence[i+1:i+2]:
            if not len(lis) or v != lis[-1]:
                lis.append(v)
        else:
            if not len(lis) or v != lis[-1]:
                lis.append(v)
    return lis



print(unique_in_order('AAAABBBCCDAABBB'))

def unique_in_order(sequence):
   return [z for i, z in enumerate(sequence) if i == 0 or sequence[i - 1] != z]

print(unique_in_order('AAAABBBCCDAABBB'))