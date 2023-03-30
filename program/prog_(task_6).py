def set_alarm(employed, vacation):
    return False if vacation == True or vacation == False and employed == False else True

print(set_alarm(True, True))
print(set_alarm(False, True))
print(set_alarm(False, False))
print(set_alarm(True, False))




