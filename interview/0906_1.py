def ArrayChallenge(arr):
    if len(arr) < 3:
        return -1  # Not enough elements to determine a sequence

    is_arithmetic = True
    is_geometric = True

    if arr[0] == 0:
        is_geometric = False

    arithmetic_diff = arr[1] - arr[0]
    geometric_ratio = arr[1] / arr[0] if arr[0] != 0 else None

    for i in range(1, len(arr) - 1):
        if arr[i + 1] - arr[i] != arithmetic_diff:
            is_arithmetic = False
        if arr[i] == 0:
            is_geometric = False
            break
        if arr[i + 1] / arr[i] != geometric_ratio:
            is_geometric = False

    if is_arithmetic:
        return "Arithmetic"
    elif is_geometric:
        return "Geometric"
    else:
        return -1


# Test the function
print(ArrayChallenge([5, 10, 15]))  # Should print "Arithmetic"
print(ArrayChallenge([2, 4, 16, 24]))  # Should print -1
print(ArrayChallenge([2, 6, 18, 54]))  # Should print "Geometric"
