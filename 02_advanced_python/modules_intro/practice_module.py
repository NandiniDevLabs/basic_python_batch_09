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

# Calling test function
test()

print("This is last line from practice_module file.")