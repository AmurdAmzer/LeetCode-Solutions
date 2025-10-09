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

# 3. Array Solution (Time O(n); space O(1) since the character set is fixed)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        # step 1: check if the length of the two strings are the same, if yes, continue, if no, return false.
        if len(s) != len(t):
            return False

        # step 2: create an array of numbers (0s) to collect the frequencies/counts of each character in both strings
        array = [0] * 26

        # step 3: check for the characters in the strings and add for s and subtract for t
        for i in range(len(s)):
            array[ord(s[i]) - ord('a')] += 1
            array[ord(t[i]) - ord('a')] -= 1

        # step 4: check to see if the values in the array are all 0s, if they are 0s, anagram, return true, else, return false
        for val in array:
            if val != 0:
                return False
        return True