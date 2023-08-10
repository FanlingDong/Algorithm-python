"""
Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]


"""


def findMissingRanges(nums, lower, upper):
    def findRange(low, high):
        if low == high:
            return str(low)
        return f'{low} -> {high}'

    if not nums:
        return f'{lower} -> {upper}'

    res = []

    if nums[0] > lower:
        res.append(findRange(lower, nums[0] - 1))

    for prev, curr in zip(nums, nums[1:]):
        print(prev, curr)
        if prev < curr - 1:
            res.append(findRange(prev + 1, curr - 1))

    if nums[-1] < upper:
        res.append(findRange(nums[-1] + 1, upper))

    return res

print(findMissingRanges([0, 1, 3, 50, 75], 0, 99))



