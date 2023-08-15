"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8

"""

def generateParenthesis(n: int):
    # open close
    #         (0,0) ''
    #         (1,0) '('
    # (2,0)'(('   (1,1)'()'
    #     (2,1)'(()'  (2,1) '()('
    #         (2,2)'(())'   (2,2)'()()'

    res = []

    def dfs(open, close, string):
        if len(string) == n * 2:
            res.append(string)
            return

        if open < n:
            dfs(open + 1, close, string + '(')

        if close < open:
            dfs(open, close + 1, string + ')')

    dfs(0, 0, '')
    return res
