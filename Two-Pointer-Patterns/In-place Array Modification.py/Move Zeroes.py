## 283. Move Zeroes

'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]
'''

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        '''
        1. Two Pointers + Array Modification
            - we use a two ptr approach to move all of the zeroes to the end of the array while also maintaining the relative order of the non-zero elements. our right ptr will go through array and search for non-zero elements while the left ptr will let us know the position of where to put the non-zero element. 
            - Time Complexity: O(n) because our outer loop with ptr 'R' will run through approximately the whole length of nums. 
            - Space Complexity: O(1) since we are only using a few ptrs to modify the array in place
        '''

        L = 0
        for R in range(len(nums)):
            if nums[R] != 0:
                nums[L], nums[R] = nums[R], nums[L]
                L += 1