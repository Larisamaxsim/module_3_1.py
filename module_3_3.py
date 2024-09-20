def print_params(a = 1, b = 'Строка', c = True):
    print(a, b, c)

print_params()
print_params(b=25)
print_params(c = [1,2,3])

value_list = [[3,2],'Строка',True]
value_dict = {'a' : 'Строка', 'b': True, 'c': 25.2}
values_list_2 = [54.32, 'Строка' ]
print_params(*value_list)
print_params(**value_dict)
print_params(*values_list_2, 42)