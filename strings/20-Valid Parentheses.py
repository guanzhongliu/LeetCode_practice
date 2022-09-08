'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true
'''


class Solution:
    # 其实可以用stack，更简单更快
    def isValid(self, s: str) -> bool:
        ans_list = []
        bw = {'}': '{', ')': '(', ']': '['}
        for i in s:
            if i in bw:
                if len(ans_list) == 0 or bw[i] != ans_list[-1]:
                    return False
                else:
                    ans_list = ans_list[:-1]
            else:
                ans_list.append(i)
        return len(ans_list) == 0
