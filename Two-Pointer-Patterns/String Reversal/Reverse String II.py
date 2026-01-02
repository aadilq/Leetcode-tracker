## 541. Reverse String II

'''
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

 

Example 1:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Example 2:
Input: s = "abcd", k = 2
Output: "bacd"
'''

class Solution:
    def reverseStringII(self, s: str, k: int) -> str:
        '''
        1. Two Pointers + String Reversal
            - we have to first convert our string into a list in order to change the first k character of 2*k, we iterate through the string, each time going 2*k, we reverse the first k character and move on to the next 2*k characters.
            - Time Complexity: Converting the string s into a list of characters takes O(n) time, where n is the length of s. The for loop iterates over the string in steps of 2*k, resulting in approximately n/(2*k) iterations the overall time complexity is dominated by the list conversion and the reversal operations, resulting in O(n).
            - Space Complexity: O(n) Converting the string into a list of characters requires O(n) space.
        '''
        s = [char for char in s]
        for i in range(0, len(s), 2*k):
            s[i:i+k] = reversed(s[i:i+k])
        return "".join(s)
solution = Solution()
print(solution.reverseStringII("abcdefg", 2))