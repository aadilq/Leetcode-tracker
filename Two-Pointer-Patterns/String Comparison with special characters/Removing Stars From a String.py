## 2390. Removing Stars From a String

'''
You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:

The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.
 

Example 1:
Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".

Example 2:
Input: s = "erase*****"
Output: ""
Explanation: The entire string is removed, so we return an empty string.
'''

class Solution:
    def removeStars(self, s: str) -> str:
        '''
        1. Two Pointer + special character comparison
            - in order to remove the left character whenever we encounter a star, we can use a stack. each time we encounter a star, we check if our stack is populated and then pop from our stack. if we encounter a alphabetical character, we append it our stack. at the end our string, we convert our stack into a string and return the string. 
            - Time Complexity: O(n) where n is the length of input string. this is because we are iterating to the end of the input string and performing stack operation which are O(1). 
            - Space Complexity: O(n) where n is the length of input string. this is because worst case, our input string does not contain any stars and our stack becomes as big as our input string. 
        '''

        stack = []

        for char in s:
            if stack and char == "*":
                stack.pop()
            else:
                stack.append(char)
        string = "".join(stack)
        return string
solution = Solution()
print(solution.removeStars("leet**cod*e"))