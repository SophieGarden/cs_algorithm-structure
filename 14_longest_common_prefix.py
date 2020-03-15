14. Longest Common Prefix
Easy

2079

1688

Add to List

Share
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

Accepted
653,858
Submissions
1,883,652

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        i = 0
        flag = True
        while True:
            for s in strs:
                if i > len(s)-1 or s[i] != strs[0][i]:
                    flag = False
                    break
            if len(strs) > 0 and flag:
                res += s[i]
                i += 1
            else:
                break
        return res

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        i = 0
        flag = True
        while True:
            for s in strs:
                if i > len(s)-1 or s[i] != strs[0][i]:
                    flag = False
                    break
            if flag:
                i += 1
            else:
                break
        return strs[0][0:i]
                
