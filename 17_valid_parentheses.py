'''20. Valid Parentheses
Easy

4308

202

Add to List

Share
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
Accepted
885,934
Submissions
2,321,604
'''
class Solution:
    def isValid(self, s: str) -> bool:
        left = ['(', '{', '[']
        right = [')', '}', ']']
        d = {r: l for l, r in zip(left, right)}
        stack = []
        for char in s:
            if char in d:
                last_element = stack.pop() if stack else '#'
                if d[char] != last_element:
                    return False
            else:
                stack.append(char)
        return True if len(stack)==0 else False
class Solution:
    def isValid(self, s: str) -> bool:
        def _inner_isValid(s):
            if len(s) == 0:
                return True
            left = ['(', '{', '[']
            right = [')', '}', ']']
            d = {r: l for l, r in zip(left, right)}
            s_temp = s
            for i in range(1, len(s)):
                prev, cur = s[i-1], s[i]
                if cur in right and prev == d[cur]:
                    return _inner_isValid(s[:i-1] + s[i+1:])
            return False
        return _inner_isValid(s)

