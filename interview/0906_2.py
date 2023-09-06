def is_covering_number(num):
    # Convert the number to a string to work with its digits
    num_str = str(num)

    # Get the length of the number and count of nonzero digits
    n = len(num_str)
    nonzero_digits = set(num_str) - {'0'}

    # Check if it's a covering number
    if len(nonzero_digits) == n - num_str.count('0'):
        return num_str.count('0')
    else:
        return -1


# Test cases
print(is_covering_number(1423))  # Output: 0
print(is_covering_number(12346500))  # Output: 2