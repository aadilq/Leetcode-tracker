## 11. Container With Most Water

'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
'''

class Solution:
    def maxArea(self, height: list[int]) -> int:
        '''
        1. Nested for loops- Brute Force 
            - Using a nested for loop to check every pair of heights to find the max area. Inefficient for large array sizes. 
            
            - Time Complexity: O(n^2) because for each element, we iterate through all of the other elements. 
            - Space complexity: O(1), as the algorithm uses only a fixed amount of extra space
        '''`
        '''
        2. Two Pointer Approach (Converging) - Optimal Approach
            - Initialize two pointers at the beginning and end of the height array. Calculate the current area with the minimum height
            of the two pointers. move whichever pointer has the smaller height.

            - Time Complexity: O(n) since our two pointer approach initializes two pointers at the start and end of the array and converges towards the middle. depends on the size of the height array
            Space Complexity: O(1) The algorithm uses a constant amount of extra space for variables such as maxArea, L, R, and currentArea.
        '''
        maxArea = 0

        L, R = 0, len(height) - 1

        while L < R:
             currentArea = ((R - L) * min(height[L], height[R]))
             maxArea = max(maxArea, currentArea)

             if height[L] <= height[R]:
                L += 1
             else:
                R -= 1
        return maxArea
