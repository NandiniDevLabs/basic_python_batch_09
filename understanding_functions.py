def filter_even_numbers(numbers):
    print("This is start of filter_even_numbers")
    print(f"Input received is {numbers}") # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    even_numbers = [num for num in numbers if num%2==0]  # [2, ]
    print(f"Numbers to be returned {even_numbers}")
    print("This is end of filter_even_numbers")
    return even_numbers
##

def filter_odd_numbers(i):
    print("This is start of filter_odd_numbers")
    print(f"Input numbers: {i}")
    odd_numbers = [num for num in i if num%2==1]
    print(f"Values to be returned: {odd_numbers}")
    print("This is end of filter_odd_numbers")
    return odd_numbers
##



# Main Program
input_list = list(range(1,11))
print(input_list)
print("\n")

# even_list = []
# odd_list = []
if len(input_list) > 0:
    even_list = filter_even_numbers(input_list)
    odd_list = filter_odd_numbers(input_list)
    print(f"Even numbers: {even_list}")
    print(f"Odd numbers: {odd_list}")
else:
    print("Input list is empty and hence there are no even and odd numbers to print")
# Main Program