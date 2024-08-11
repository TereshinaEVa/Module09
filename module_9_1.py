def apply_all_func(int_list, *functions):
    dict_all = {}
    for func_on in functions:
        name = func_on.__name__
        dict_all[name] = func_on(int_list)
    return dict_all

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))