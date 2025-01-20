print("This is first line of practice_module2 file.")
month = 'January'
year = '2025'

def get_longest_string2(input_strs):
    longest_str = ''
    for input_str in input_strs:
        if len(input_str) > len(longest_str):
            longest_str = input_str
    #
    return longest_str
# End of get_longest_string

def test2():
    print("This is test2 function")
    print("It returns month")
    return month, year

def test3():
    print("This is test3 function")
    print("It returns month")
    return month + year

def test4():
    print("This is test4 function")
    print("It returns month")
    return month + ' ' + year

def test5():
    print("This is test5 function")
    print("It returns month")
    return month + ', ' + year

class MyClass:
    pass

print("This is last line of practice_module2 file.")