first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(len_elem) for len_elem in first_strings if len(len_elem) >= 5]
second_result = [(one_elem, two_elem) for one_elem in first_strings for two_elem in second_strings if len(one_elem) == len(two_elem)]
third_result = {elem: len(elem) for elem in first_strings + second_strings if len(elem) % 2 ==0}

print(first_result)
print(second_result)
print(third_result)