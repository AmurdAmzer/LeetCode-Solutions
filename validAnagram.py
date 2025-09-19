'''Valid Anagram
Solved 
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters. '''


# 1. Sorting Solution (Time O(nlogn); space O(1) or O(n) depending on the sorting algorithm)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

        
# 2. Counter Solution (Time O(n); space O(n))
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        from collections import Counter
        
        sCounter = Counter(s)
        tCounter = Counter(t)
        return sCounter == tCounter

# 3. HashMap Solution (Time O(n); space O(1) since the character set is fixed)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True