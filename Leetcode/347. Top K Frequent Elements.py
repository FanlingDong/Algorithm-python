# solution:https://www.youtube.com/watch?v=YPTqKIgVk-k


def topKFrequent(nums, k):
    # use heap and bucket sort
    # counts: 1     2     3      4      5    6
    # array: [3]  [2,2]  [1,1,1]
    freq = [[] for i in range(len(nums) + 1)]
    count = {}
    for num in nums:
        count[num] = 1 + count.get(num, 0)

    for n, c in count.items():
        # count would be the index
        freq[c].append(n)

    res = []

    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
    return res
