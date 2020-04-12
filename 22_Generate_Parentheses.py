22. Generate Parentheses
Medium

4422

241

Add to List

Share
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
Accepted
495,384
Submissions
818,489

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generateAll(s=[]):
            if len(s) == 2*n:
                if isValid(s):
                    res.append(''.join(s)) 
            else:
                s.append('(')
                generateAll(s)
                s.pop()
                s.append(')')
                generateAll(s)
                s.pop()
            
        def isValid(s):
            bal = 0
            for p in s:
                if p == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:
                    return False
            return bal == 0
            

        res = []
        generateAll()
        return res
            
            
            
        def backtracking(s, cnt_l, cnt_r):
            if len(s) == 2*n:
                res.append(s)
            if cnt_l < n:
                backtracking(s+'(', cnt_l+1, cnt_r)
            if cnt_r < cnt_l:
                backtracking(s+')', cnt_l, cnt_r+1)
        
        res = []
        backtracking('(', 1, 0)
        return res
            

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        res = []
        for c in range(n):
            for pairs_l in self.generateParenthesis(c):
                for pairs_r in self.generateParenthesis(n-1-c):
                    res.append('({}){}'.format(pairs_l, pairs_r))
        return res
                    
        
            
        
