## 438. Find All Anagrams in a String

'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

 

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        '''
        1. character frequency matching
            - we first want to check if the len of string s is bigger than len of string p. if not, return an empty list because p's anagrams cannot exist in s. then we initialize two hashmaps, one to count the frequency of characters in string s and in string p. for our initial check, we check the frequency of characters in both string up to the length of string p. if the hashmaps are the same, we initialize a res array filled with 0. we then check every substring of size len(p)
            - Time Complexity: O(n + m) where n is the length of string p and m is the string s. this is because we iterating through both strings to see how many anagrams of p exists within s. 
            - Space Complexity: O(n) where n is the length of string p. this is because the size of our hashmap will never exceed the length of p
        '''

        if len(p) > len(s):
            return []
        
        Scount, Pcount = {}, {}

        for i in range(len(p)):
            Scount[s[i]] = Scount.get(s[i], 0) + 1
            Pcount[p[i]] = Pcount.get(p[i], 0) + 1
        res = [0] if Scount == Pcount else []

        L = 0 
        for R in range(len(p), len(s)):
            Scount[s[R]] = Scount.get(s[R], 0) + 1
            Scount[s[L]] -= 1
            if Scount[s[L]] == 0:
                del Scount[s[L]]
            L += 1
            if Scount == Pcount:
                res.append(L)
        return res

solution = Solution()
print(solution.findAnagrams("cbaebabacd", "abc"))