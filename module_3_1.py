calls = 0
def count_calls():
    global calls
    calls = calls+1


def string_info(string):
    karteg = (len(string), string.upper(), string.lower())
    count_calls()
    return karteg


def is_contains(string, list_to_search):
    string = string.upper()
    list_to_search = [s.upper() for s in list_to_search]
    result = string in list_to_search
    count_calls()
    return result


result1 = string_info('Capybara')
result2 = string_info('Armageddon')
result3 = is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
result4 = is_contains('cycle', ['recycling', 'cyclic'])
print(result1)
print(result2)
print(result3)
print(result4)
print(calls)
