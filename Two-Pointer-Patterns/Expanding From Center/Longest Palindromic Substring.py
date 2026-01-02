## 5. Longest Palindromic Substring

'''
Given a string s, return the longest palindromic substring in s.

 

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        1. Two Pointers + Expanding from center
            - in order to find the longest palindromic substring, we can treat every single character in our string as the middle character. for odd palindromic substrings, we initialize two pointers, left and right at the character and expand outwards. we update the maximum palindromic substring we have found so far. so even palindromic substrings, we initialize our left and right pointers to be at the current character and the character to the right of it because we have to have two adjacent characters be the same. 
            - Time Complexity: O(n) where n is the length of the input string. this because we iterate through each character in the input string and we treat each character as the middle character in find palindromic substrings. 
            - Space Complexity: O(1) since we are not using any additional data structures, only a few ptrs to find the palindromic substrings within our string.
        '''
        res = ""
        reslen = 0

        for i in range(len(s)):
            ##Odd Palindromic substrings
            L = R = i
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if R - L + 1 > reslen:
                    reslen =  R - L + 1
                    res = s[L:R+1]
                L -= 1
                R += 1
            ##Even Palindromic substrings
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if R - L + 1 > reslen:
                    reslen = R - L + 1
                    res = s[L:R+1]
                L -= 1
                R += 1
        return res

solution = Solution()
print(solution.longestPalindrome("babad"))