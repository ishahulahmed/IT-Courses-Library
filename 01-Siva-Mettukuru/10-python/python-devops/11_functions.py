# def sample_func():
#     print("This is a sample function")

# Call the function
# sample_func()

# def add(num_1, num_2):
#     # DOcString - To Explain What a function does
#     """
#     This function performs addtion of 2 numbers
#     """
#     res = num_1 + num_2
#     return res

# Call the function
# res = add(1, 2)
# res = add(num_2=1, num_1=2)
# print(res)

# help(add)
# Help on function add in module __main__:

# add(num_1, num_2)
#     This function performs addtion of 2 numbers

# def add(num_1, num_2, num_3=10):
#     # DOcString - To Explain What a function does
#     """
#     This function performs addtion of 2 numbers
#     """
#     res = num_1 + num_2 + num_3
#     return res

# # Call the function
# # res = add(1, 2)
# # res = add(num_2=1, num_1=2)
# # print(res)

# One user enters 10 numbers and another user enters 100 numbers.
# Define your function to handle this situation
# Answer: Variable length Arguments

# def add(*nums):
#     # DOcString - To Explain What a function does
#     """
#     This function performs addtion of 2 numbers
#     """
#     res = sum(nums)
#     return res

# res = add(1, 2, 4)
# print(res)

# res = add(1, 2, 3, 4, 5, 6)
# print(res)

# def add(num1, num2, *args):
#     # DOcString - To Explain What a function does
#     """
#     This function performs addtion of 2 numbers
#     """
#     res = num1 + num2 + sum(args)
#     return res

# res = add(1, 2, 4)
# print(res)

# res = add(1, 2, 3, 4, 5, 6)
# print(res)

def add(*args, **kwargs):
    # DOcString - To Explain What a function does
    """
    This function performs addtion of 2 numbers
    """
    print(args, kwargs)

#kwargs --> keyword arguments

res = add(1, 2, 4)
print(res)

res = add(1, 2, 3, 4, num1=5, num2=6)
print(res)

"""
Output:
(1, 2, 4) {}
None
(1, 2, 3, 4) {'num1': 5, 'num2': 6}
"""
# In a function func(num1=2, num2=4) here num1, num2 go as key value pairs


# map --> Learn Yourself
# filter --> Learn Yourself

# Lambda: inline function

add_numbers = lambda num1, num2: num1 + num2
res = add_numbers(1, 2)
print(res)

