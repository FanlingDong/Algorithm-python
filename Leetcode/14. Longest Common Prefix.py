"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""


def longestCommonPrefix(strs) -> str:
    res = ""
    for i in range(len(strs[0])):  # 遍历第一个字符串里的字符
        for s in strs:  # 得到每一个字符串
            if i == len(s) or strs[0][i] != s[i]:
                return res
        res += strs[0][i]
    return res
