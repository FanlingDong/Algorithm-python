"""
Given an array A of length n & an integer S,
check if there exist 4 elements (a,b,c & d) in A
s.t. a+b+c+d = S.
"""


# Two ways, one is array, other is hashmap

# Method 1: 1 Array + Binary search

def fourSumArray(A, S):
    sumPairs = []
    n = len(A)
    for i in range(n - 1):
        for j in range(i, n):
            if i != j:
                sumPairs.append((A[i] + A[j], i, j))

    sumPairs.sort(key=lambda x: x[-1])

    for i in range(n - 1):
        for j in range(1, n):
            cur_sum = A[i] + A[j]
            target = S - cur_sum

            left, right = 0, n - 1
            while left < right:
                mid = (left + right) // 2
                if sumPairs[mid][0] == target and i != j:
                    # Check for non-overlapping indices
                    p1, p2 = sumPairs[mid][1], sumPairs[mid][2]
                    if p1 != i and p1 != j and p2 != i and p2 != j:
                        return p1, p2, i, j
                    left += 1
                    right -= 1
                elif sumPairs[mid][0] < target:
                    left += 1
                else:
                    right -= 1
        return False


# print(fourSumArray([1, 2, 3, 4, 5, 6, 7, 8], 13))


def fourSumDict(A, S):
    sumParisDict = {}
    n = len(A)
    for i in range(n - 1):
        for j in range(i, n):
            if i != j:
                if A[i] + A[j] not in sumParisDict:
                    sumParisDict[A[i] + A[j]] = [(i, j)]
                else:
                    sumParisDict[A[i] + A[j]].append((i, j))

    for i in range(n - 1):
        for j in range(i, n):
            target = S - A[i] - A[j]
            if i != j and target in sumParisDict:
                for pair in sumParisDict[target]:
                    p1, p2 = pair[0], pair[1]
                    if p1 != i and p1 != j and p2 != i and p2 != j:
                        return p1, p2, i, j
    return False


print(fourSumDict([1, 2, 3, 4, 5, 6, 7, 8], 13))



