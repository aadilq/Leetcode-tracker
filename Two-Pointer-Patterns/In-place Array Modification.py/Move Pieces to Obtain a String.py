## 2337. Move Pieces to Obtain a String

'''
You are given two strings start and target, both of length n. Each string consists only of the characters 'L', 'R', and '_' where:

The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space directly to its left, and a piece 'R' can move to the right only if there is a blank space directly to its right.
The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.
Return true if it is possible to obtain the string target by moving the pieces of the string start any number of times. Otherwise, return false.

 

Example 1:

Input: start = "_L__R__R_", target = "L______RR"
Output: true
Explanation: We can obtain the string target from start by doing the following moves:
- Move the first piece one step to the left, start becomes equal to "L___R__R_".
- Move the last piece one step to the right, start becomes equal to "L___R___R".
- Move the second piece three steps to the right, start becomes equal to "L______RR".
Since it is possible to get the string target from start, we return true.

Example 2:

Input: start = "R_L_", target = "__LR"
Output: false
Explanation: The 'R' piece in the string start can move one step to the right to obtain "_RL_".
After that, no pieces can move anymore, so it is impossible to obtain the string target from start.

Example 3:

Input: start = "_R", target = "R_"
Output: false
Explanation: The piece in the string start can move only to the right, so it is impossible to obtain the string target from start.
'''

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        '''
        1. Two Pointer + Array Modification
            - we can use two pointers that start at the beginning of each string, we iterate until we reach the end of either string. we first check whether the character that we are on is a blank space. if it is a blank space, we keep on iterating until we get to a left or right character. If the characters don't match, we automatically return False. Next, we check that if the position in the start string is less than the position in the target string and we are on a "L", then we automatically return False as well. 
            - Time Complexity: O(n) where n is the length of string start which is the same length as string target, this is because we iterate through both string using two pointers. 
            - Space Complexity: O(1) since we only using two pointers to iterate through both strings and not any additional data structures. 
        '''

        i = j = 0 

        while i < len(start) and j < len(target):
            while i < len(start) and start[i] == "_":
                i += 1
            while j < len(start) and target[j] == "_":
                j += 1
            
            if i == len(start) or j == len(target):
                break

            if start[i] != target[j]:
                return False
            if start[i] == "L" and i < j:
                return False
            if start[i] == "R" and i > j:
                return False
        return i == len(start) and j == len(target)
solution = Solution()
print(solution.canChange("_L__R__R_", "L______RR"))