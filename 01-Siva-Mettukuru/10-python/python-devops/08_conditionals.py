# Calculate whether the given number is greater than 10 or not

user_input = int(input("Enter a number:"))
# user_input = int(user_input)

# if user_input > 10:
#     print("User input value is greater than 10")
# else:
#     print("User input value is less than or equal to 10")

"""
indentation Tab or 2 or 4 spaces
Recommended 4 spaces
{

}
"""
# Check whether the given number is equal to 10 or greater than 10 ro less than 10 or something else

# Method 1: Nested if-else
if user_input == 10:
    print("Right on target")
else:
    if user_input > 10:
        print("User input values i greater than 10")
    else:
        if user_input < 10:
            print("User input vlaue is less than 10")

# Method 2
if user_input == 10:
    print("Right on target")
elif user_input > 10:
    print("User input values i greater than 10")
else:
    print("User input vlaue is less than 10")

# Exception Handling: try - except
try:
    user_input = int(input("Enter a number:"))
    if user_input == 10:
        print("Right on target")
    elif user_input > 10:
        print("User input values i greater than 10")
    else:
        print("User input vlaue is less than 10")
except ValueError:
    # except: it will handle all errors
    # but it is not recommended 
    # specify the error
    print("Please enter a number")


