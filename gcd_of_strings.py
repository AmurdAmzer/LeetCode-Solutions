"""For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters."""



class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        len1 = len(str1)
        len2 = len(str2)

        def isDivisor(L):
            if len1 % L or len2 % L:
                return False
            f1, f2 = len1 // L, len2 // L
            return str1[:L]*f1 == str1 and str1[:L] * f2 == str2

        for L in range(min(len1, len2), 0, -1):
            if isDivisor(L):
                return str1[:L]
        return ""