## 1598. Crawler Log Folder


'''
The Leetcode file system keeps a log each time some user performs a change folder operation.

The operations are described below:

"../" : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
"./" : Remain in the same folder.
"x/" : Move to the child folder named x (This folder is guaranteed to always exist).
You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.

The file system starts in the main folder, then the operations in logs are performed.

Return the minimum number of operations needed to go back to the main folder after the change folder operations.

 

Example 1:

Input: logs = ["d1/","d2/","../","d21/","./"]
Output: 2
Explanation: Use this change folder operation "../" 2 times and go back to the main folder.

Example 2:

Input: logs = ["d1/","d2/","./","d3/","../","d31/"]
Output: 3

Example 3:

Input: logs = ["d1/","../","../","../"]
Output: 0
'''

class Solution:
    def minOperations(self, logs: list[str]) -> int:
        '''
        1. Two Pointer + special character comparison
            - we iterate through each operation in logs and we also set a variable called moves to keep track of our moves. if the first character of the operation is not equal to '.', it means that we are moving into a child folder, so increase our moves variable by 1. we also check if the first two characters are equal to '..' meaning that we moving into our parent folder so we decrease our moves variable by 1 but we only decrease our moves variable if it is greater than 0.
            - Time Complexity: O(n) where n is the number of operations in the input array. this is because we are iterating through each operation
            - Space Complexity: O(1) because we are not using any additional data structures, only variables to keep track of our moves
        '''
        moves = 0 

        for operation in logs:
            if operation[0] != '.':
                moves += 1
            elif operation[0:2] == '..':
                if moves > 0:
                    moves -= 1
        return moves
solution = Solution()
print(solution.minOperations(["d1/","d2/","../","d21/","./"]))