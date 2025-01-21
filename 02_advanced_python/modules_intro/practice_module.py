print("This is first line of practice_module file.")

def get_longest_string(input_strs):
    longest_str = ''
    for input_str in input_strs:
        if len(input_str) > len(longest_str):
            longest_str = input_str
    #
    return longest_str
# End of get_longest_string

# Defining test function
def test():
    print("This is test function")
    print("It returns None")
    return None

def test2():
    print("This is test2 function from practice_module")
    print("It returns None")
    return None

def test3():
    my_test3_var = 5.2
    print("This is test3 function from practice_module")
    print("It returns None")
    print(f"My test3 variable is : {my_test3_var}")
    return None

# Calling test function
test()

print("This is last line from practice_module file.")