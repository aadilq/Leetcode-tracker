## 75. Sort Colors

'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
'''

class Solution:
    def sortColors(self, nums: list[int]) -> list[int]:
        '''
        1. Two Pointer + Array Modification 
            - we initialize three variables (red, white, and blue) to keep track of how many of each color we have. we do two passes of the array. the first pass counts how many of each color we have. the second pass reorganizes the array in the order red, white, and blue.
            - Time Complexity: O(n) where n is the length of the input array. This is because we do separate passes through the array
            - Space Complexity: O(1) since we are only using a few ptrs to keep track how many of each color we have
        '''
        red = white = blue = 0

        for num in nums:
            if num == 0:
                red += 1
            elif num == 1:
                white += 1
            else:
                blue += 1
        
        for i in range(len(nums)):
            if red > 0:
                nums[i] = 0
                red -= 1
            elif white > 0:
                nums[i] = 1
                white -= 1
            else:
                nums[i] = 2
                blue -= 1
        return nums

solution = Solution()
print(solution.sortColors([2,0,2,1,1,0]))