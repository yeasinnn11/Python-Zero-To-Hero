def avg(*args):
    if not args:
        raise ValueError("At least one argument must be passed")
    return sum(args) / len(args)

# Read space-separated integers from input
input_args = input().split()

# Convert input arguments to integers
numbers = list(map(int, input_args))

# Check if at least one number was provided
if not numbers:
    print("At least one number must be provided.")
else:
    # Calculate the average using the avg function
    average_value = avg(*numbers)
    # Print the average with two decimal places
    print('{:.2f}'.format(average_value))
