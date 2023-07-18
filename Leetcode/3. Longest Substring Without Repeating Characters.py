def lengthOfLongestSubstring(s: str) -> int:
    # a b c a b c b b
    #   l
    char_set = set()
    left = 0
    result = 0

    for r in range(len(s)):  # r = 3
        while s[r] in char_set:  # char_set = a b c
            char_set.remove(s[left])
            left += 1
        char_set.add(s[r])  # b c a
        result = max(result, r - left + 1)  # 3
        print(char_set)
    return result
