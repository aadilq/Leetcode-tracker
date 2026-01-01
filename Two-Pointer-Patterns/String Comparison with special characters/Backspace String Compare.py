## 844. Backspace String Compare

'''
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        '''
        1. Two Pointer + special character comparison
            - the idea is to use two ptrs that start at the end of each string and work towards the beginning. we initialize two ptrs that start at the end of each string. we also initialize two variables (skipS & skipT) that keep track of how many backspace characters we have encountered so far. we start checking the characters in both strings. if the current character is a backspace character, we increment our backspace variable by 1 and decrement our character to move on to the next character. now we check if the backspace variable is greater than 1. if it is greater than 1, this means that we have skip over our current character and decrement our backspace variable. else, if the backspace variable is 0 and the current character is not a backspace character, its a valid character. we do this for both s and t. we check the characters to see if they are equal.
            - Time Complexity: O(n + m) where n is length of string s and m is the length of string t. this is because we are iterating backwards to forwards through both strings. 
            - Space Complexity: O(1) since we are using a few ptrs to keep track of each character in both strings. 
        '''
        i, j, = len(s) - 1, len(t) - 1
        skipS = skipT = 0

        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == "#":
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if t[j] == "#":
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break
            
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False
            i -= 1
            j -= 1
        return True
solution = Solution()
print(solution.backspaceCompare("ab#c", "ad#c"))
                
