def calculate_years(principal, interest, tax, desired):
    if principal >= desired:
        return 0
    return 1 + calculate_years(principal + (principal * interest - (principal * interest * tax)),interest,tax,desired)


start = [1000, 0.05, 0.18, 1100]

print(calculate_years(1000, 0.05, 0.18, 1100))
# print(1000 * .05 - (1000 * .05 *.18) )