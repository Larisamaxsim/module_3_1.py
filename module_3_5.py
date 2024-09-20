def get_multiplied_digits(number):
    str_number = str(number)
    str_number = str_number.replace('0', '')
    if str_number == '':
        return 'Введите число больше 0'
    first = int(str_number[0])
    if len(str_number) > 1:
       return first * get_multiplied_digits(int(str_number[1:]))
    else:
       return first


print(get_multiplied_digits(40203))