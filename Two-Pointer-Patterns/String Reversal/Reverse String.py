## 344. Reverse String

'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
'''

class Solution:
    def reverseString(self, s: list[str]) -> list[str]:
        '''
        1. Two Pointer + String Reversal
            - to modify the array in place, we can establish two pointers at the beginning and end of the array. we swap the characters at the pointers and we shift our pointers inwards and continue swapping until we reach the middle of the array. 
            - Time Complexity: O(n) where n is the length the list. this is because we start at both ends of the array and work inwards. 
            - Space Complexity: O(1) since we are only left and right pointers to perform our swaps. 
        '''
        L, R = 0, len(s) - 1

        while L < R:
            s[L], s[R] = s[R], s[L]
            L += 1
            R -= 1
        return s
solution = Solution()
print(solution.reverseString(["h","e","l","l","o"]))