def all_variants(text):
    for size in range(len(text)):
        for lit in range(len(text) - size):
            yield text[lit:lit + size + 1]



a = all_variants("abcd")
for i in a:
    print(i)