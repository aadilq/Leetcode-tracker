## 647. Palindromic Substrings

'''
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
'''

class Solution:
    def countSubstrings(self, s: str) -> str:
        '''
        1. Two Pointers + Expanding outwards
            - in order to count how many palindromic substrings exist within the input strings, we have to consider both odd and even palindromic substrings. we iterate through each character and for odd palindromic substrings, we use a left and right pointer where the left and right pointer are at the current character. if the character matches, then we move our left pointer down by 1 and our right pointer up by 1. for even palindromic substrings, we consider if adjacent characters are the same. we set our left and right pointers to the current character and the character to the right of it. if they are the same, we increment the number of palindromic substrings and shift our pointers. 
            - Time Complexity: O(n^2) where n is the length of the input string. this because we iterate through each character in the input string and we treat each character as the middle character and the inner while loops expand outward to check for palindromes. In the worst case, each expansion can go up to the entire length of the string.
            - Space Complexity: O(1) since we are not using any additional data structures, only a few ptrs to find the palindromic substrings within our string.
        '''

        res = 0 

        for i in range(len(s)):
            ##Odd Palindromic substrings
            L = R = i
            while L >= 0 and R < len(s) and s[L] == s[R]:
                res += 1
                L -= 1
                R += 1
            ##Even Palindromic substrings
            L, R = i, i+1
            while L >= 0 and R < len(s) and s[L] == s[R]:
                res += 1
                L -= 1
                R += 1
        return res
solution = Solution()
print(solution.countSubstrings("aaa"))