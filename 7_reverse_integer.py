7. Reverse Integer
Easy

2882

4518

Add to List

Share
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows

class Solution:
    def reverse(self, x: int) -> int:

        sign = -1 if x < 0 else 1
        x *= sign
        n = 0
        while x > 0:
            n = n*10 + x % 10
            x = x // 10
        n *= sign
        return 0 if n < -2**31 or n > 2**31-1 else n.
