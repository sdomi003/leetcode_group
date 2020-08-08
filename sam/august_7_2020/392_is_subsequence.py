'''
Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 10^4
Both strings consists only of lowercase characters.
'''



class Solution:
    def two_pointer_solution(self, s:str, t:str) -> bool:
        p1 = 0
        p2 = 0
        while (p1 < len(s) and p2 < len(t)):
            if (s[p1] == t[p2]):
                p1 += 1
            p2 += 1
        if (p1 == len(s)):
            return True
        return False
        
    def dynamic_programming_solution(self, s: str, t: str) -> bool:
        '''
        Dynamic Programming should not be used for this problem.
        I implemented it as an exercise.
        This problem can be viewed as a simpler version of a Hard question that does require DP.
           # a s g b k l c
        #  0 0 0 0 0 0 0 0
        a  0 1 1 1 1 1 1 1         
        b  0 1 1 1 2 2 2 2         
        c  0 1 1 1 2 2 2 3        
        '''
        dp = [[0 for i in range(len(t) + 1)] for j in range(len(s) + 1)]
        for col in range(1, len(t) + 1):
            for row in range(1, len(s) + 1):
                if (s[row - 1] == t[col - 1]):
                    dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    dp[row][col] = max(dp[row-1][col], dp[row][col-1])
        if (len(dp) < 1):
            return False
        if (dp[len(dp)-1][len(dp[0]) - 1] == len(s)):
            return True
        return False
        
        
        
        
    def isSubsequence(self, s: str, t: str) -> bool:
        #return self.two_pointer_solution(s, t)
        return self.dynamic_programming_solution(s, t)
