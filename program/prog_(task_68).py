def high(st):
    return max(st.split(), key=lambda x: sum(ord(i)-96 for i in x))

print(high('what time are we climbing up the volcano'))