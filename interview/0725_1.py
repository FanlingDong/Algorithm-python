'''
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.
# abc -> acb, bac, bca, cab, cba
# abcc - cabc

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true

# Explanation: s2 contains one permutation of s1 ("ba").

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
# - s1 and s2 consist of lowercase English letters.
'''

''' 
# Method 1 - hashmap compare
def main(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    dict_s1 = {}
    for s in s1:
        if s in dict_s1:
            dict_s1[s] += 1
        else:
            dict_s1[s] = 1

    # O(m*n)
    # dict_s2 = {}
    for i in range(len(s2)):
        if s2[i] in s1 and i + len(s1) <= len(s2):
            # compare two strings
            dict_s2 = {}
            new_s2 = s2[i: i + len(s1)]
            # dict_s2[s[i - len(s1)]] -= 1
            # dict_s2[s2[i]] += 1
            for s in new_s2:
                if s in dict_s2:
                    dict_s2[s] += 1
                else:
                    dict_s2[s] = 1
            if dict_s2 == dict_s1:
                return True
    return False
'''


# Method 2 - slide windows
def main(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    char_count_s1 = [0] * 26
    for c in s1:
        char_count_s1[ord(c) - ord('a')] += 1

    window_count = [0] * 26
    window_size = len(s1)
    for i in range(len(s2)):
        window_count[ord(s2[i]) - ord('a')] += 1
        # Window has fully slided into the s2
        if i >= window_size:
            window_count[ord(s2[i - window_size]) - ord('a')] -= 1
        if window_count == char_count_s1:
            return True
    return False


print(main('ab', 'eidbaooo'))
