## 392. Is Subsequence

'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

'''

class Solution:
    def subsequence(self, s: str, t: str) -> bool:
        '''
        1. Fast and Slow Pointer approach on both strings
            - We initially start our pointer at the start of both strings. We move both pointer if the characters match at that index. If they don't match, we move the pointer at pointer at t to find the next character where a match occurs because we are trying to see if s is a subsequence of t. 
            - Time Complexity: O(n), where n is the length of string t because in the worst case, the algorithm iterates through each character of t once
            - Space Complexity: O(1) because the algorithm uses only a fixed number of variables (i and j) regardless of the input sizes
        '''
        i = j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return True if i == len(s) else False
solution = Solution()
print(solution.subsequence("abc", "ahbgdc"))
