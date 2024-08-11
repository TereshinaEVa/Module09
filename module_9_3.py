first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(i_1) - len(i_2) for i_1, i_2 in zip(first, second) if len(i_1) != len(i_2))
second_result = (len(first[i]) == len(second[i]) for i in range(3))  # или len(first)

print(list(first_result))
print(list(second_result))