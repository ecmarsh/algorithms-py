"""
@=lc id=438 lang=python3 tag=sliding_window

[438] Find All Anagrams in a String

Given a string `s` and non-empty string `p`,
find all the start indices `p`'s anagrams in `s`.

Strings consists of lowercase English letters only, and the
length of both strings `s` and `p` will not be larger than 20,100.

The order of output does not matter.

Example 1:
    Input: s="cbaebabacd", p="abc"
    Output: [0, 6]
    Explanation: The substring w start index=0 is "cba".
                 The substring w start index=6 is "bac".

Example 2:
    Input: s="abab", p="ab"
    Output: [0, 1, 2]
    Explanation: Substring at index 0 is "ab".
                 Substring at index 1 is "ba".
                 Susbtring at index 2 is "ab".

Complexity:
    Time: O(s*p) Worst case all anagrams (ex 2), check dict s times.
          Note: commented out solution keeps track of 0's for O(s) time.
    Space: O(p) Counter for p characters.
"""


import collections

from typing import List


class Solution:
    """
    Anagram means same count of letters, order doesn't matter.
    Keep counts of p in map, use sliding window of length p,
    and track counts of letters in current window.
    When all counts are 0, valid anagram -> store left side.
    """
    def findAnagrams(self, s:str, p:str) ->List[int]:
        if len(s) == 0 or len(p) == 0:
            return []

        self.d = collections.Counter(p)
        for c in s[:len(p)]:
            if c in self.d:
                self.d[c] -= 1

        ret = [0] if self.isAnagram() else []

        lo, hi = 0, len(p)
        while hi < len(s):
            if s[hi] in self.d or s[lo] in self.d:
                if s[hi] in self.d:
                    self.d[s[hi]] -= 1
                if s[lo] in self.d:
                    self.d[s[lo]] += 1
                if self.isAnagram():
                    ret.append(lo+1)
            lo += 1
            hi += 1

        return ret

    def isAnagram(self) -> bool:
        for c in self.d:
            if self.d[c] != 0:
                return False
        return True

"""
O(s) improvement:

class Solution:
    def findAnagrams(self, s:str, p:str) ->List[int]:
        if len(s) == 0 or len(p) == 0:
            return []
        
        d, z = collections.Counter(p), 0
        for c in s[:len(p)]:
            if c in d:     
                if d[c] == 0:
                    z -= 1
                d[c] -= 1
                if d[c] == 0:
                    z += 1
                
        ret = [0] if z == len(d) else []
        
        lo, hi = 0, len(p) 
        while hi < len(s):
            if s[hi] in d or s[lo] in d:
                if s[hi] in d:
                    if d[s[hi]] == 0:
                        z -= 1
                    d[s[hi]] -= 1
                    if d[s[hi]] == 0:
                        z += 1
                if s[lo] in d:
                    if d[s[lo]] == 0:
                        z -= 1
                    d[s[lo]] += 1
                    if d[s[lo]] == 0:
                        z += 1
                if z == len(d):
                    ret.append(lo+1)
            lo += 1
            hi += 1
            
        return ret
"""       
