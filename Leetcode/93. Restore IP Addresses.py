class Solution:
    def __init__(self):
        self.result = []

    def restoreIpAddresses(self, s: str):
        self.backTracking(s, 0, 0, "", self.result)
        return self.result

    # point_sum是IP中逗点的总数，逗点总数决定了树的深度，就是3个
    # 3个逗点，4个子串，需要对最后一段子串也进行合法性的判断
    # start_index就是子串分割线，也就是逗点
    def backTracking(self, s, start_index, point_sum, current, result):
        if point_sum == 3:
            # 判断最后一段子串是否合法
            if self.isValid(s, start_index, len(s) - 1):
                current += s[start_index:]
                # 会对原始的s加逗点，然后直接将s放进结果集
                self.result.append(current)
                return
        for i in range(start_index, len(s)):
            # 判断切割的第一个子串的合法性，左闭右闭
            if self.isValid(s, start_index, i):
                # 改造字符串，插入点
                sub = s[start_index: i + 1]
                self.backTracking(s, i + 1, point_sum + 1, current + sub + '.', result)
            else:
                break

    def isValid(self, string, start, end):
        if start > end:
            return False
        if string[start] == '0' and start != end:
            return False
        num = 0
        for i in range(start, end + 1):
            if not string[i].isdigit():
                return False
            num = num * 10 + int(string[i])
            if num > 255:
                return False
        return True


sou = Solution()
s = "25525511135"

print(sou.restoreIpAddresses(s))