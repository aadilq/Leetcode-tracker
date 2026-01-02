## 345. Reverse Vowels of a String

'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:
Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:
Input: s = "leetcode"

Output: "leotcede"
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        '''
        1. Two Pointer + String Reversal
            - since strings are immutable in python, we have to convert our string into a list. then we initialize two pointers, one at the beginning of the array and one at the end. when we come across two letters that are vowels, we swap them and move our pointers. 
            - Time Complexity: O(n) where n is length of the input string. our outer loop starts at both ends of the string and works inwards, moving across the entire string. 
            - Space Complexity: O(n) because we are converting our string into a list in order to swap characters so our list can be as big as our string. 
            "IceCreAm"
             L     R
        '''
        s = [char for char in s]
        vowels = "aeiou"

        L, R = 0, len(s) - 1
        while L < R:
            while L < R and s[L].lower() not in vowels:
                L += 1
            while R > L and s[R].lower() not in vowels:
                R -= 1
            s[L], s[R] = s[R], s[L]
            L += 1
            R -= 1
        return "".join(s)
solution = Solution()
print(solution.reverseVowels("IceCreAm"))
            