'''Group Anagrams
Solved 
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]
Constraints:

1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters. '''

# Solution 1: using sorting Time O(n * k log k); space O(n)......>
# step 1: create a diffult dictionary and assign it to groups (groups of words), where the key is the sorted word/string and the value is the list of words that are the same or anagrams
         from collections import defaultdict

         groups = defaultdict(list)

         # step 2: sort the words and save the sorted words to keys, then append/add anagrams to their keys

         for word in strs:
            key = "".join(sorted(word))
            groups[key].append(word)

        
        # step 3: return the list of anagrams

         return list(groups.values())


# Solution 2: using counting Time O(n * k); space O(n)
