# Given an array of m integers, partition it into n groups such that each group contains numbers whose sum is not greater than a value v, and if a single number is greater than v, then it is grouped separately. The returned data is represented as a two-dimensional array.
#
# function split(arr, n) {
# // code
# }
#
# const arr = [1, 10, 5, 100, 25, 38, 50, 20, 15];
# split(arr, 75);
# /*
# [
# [1, 10, 5],
# [100],
# [25, 38],
# [50, 20],
# [15]
# ]
# */


def split(arr, n):
    current_sum = 0
    current_path = []
    result = []
    for i in range(len(arr)):
        if current_sum + arr[i] > n:
            result.append(current_path)
            current_path = [arr[i]]
            current_sum = arr[i]
        else:
            current_sum += arr[i]
            current_path.append(arr[i])

    if len(current_path) != 0:
        result.append(current_path)

    return result


arr = [1, 10, 5, 100, 25, 38, 50, 20, 15]
print(split(arr, 75))
