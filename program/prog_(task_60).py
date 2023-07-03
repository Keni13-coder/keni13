def duplicate_count(text):
    text = text.lower()
    return sum( 1 for x in set(text) if text.count(x)>1)
    return len(set(filter(lambda x: text.count(x) >1,text)))

print(duplicate_count("djifZ1DaoUQJi2fPLmI9ZmsFEWisfvx9uC3KLnJdlwkNzOZaLEI5vWpEtBwGKC"))
