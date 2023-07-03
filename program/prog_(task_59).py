def digital_root(n):
    if n < 10:
        return n
    return digital_root(sum(map(int,str(n))))




print(digital_root(132189))
#  test.assert_equals(digital_root(16), 7)
#         test.assert_equals(digital_root(942), 6)
#         test.assert_equals(digital_root(132189), 6)
#         test.assert_equals(digital_root(493193), 2)