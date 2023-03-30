def hero(bullets, dragons):
    return True if bullets // dragons >= 2 or dragons == 0 else False

print(hero(10, 5))
print(hero(7, 4))
print(hero(4, 5))
print(hero(100, 40))
print(hero(1500, 751))
print(hero(0, 1))