## 167. Two Sum II - Input Array Is Sorted

'''
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
'''

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        '''
        1. Nested for-loop - Brute Force
            - use a nested for loop to try out every single pair of numbers to see if their sum is equal to the target. if their sum is equal to the target, return the indices added by one since it is a one indexed array. 

            - Time Complexity: O(n ^ 2) where n is the length of the input array. our outer loop runs n times and for each iteration, our inner loop runs approximately n times. 
            - Space Complexity: O(1) since we are not using any additional data structures
        '''

        '''
        2. Two Pointer Approach (Converging)
            - since our input array is already sorted, we initialize two pointers, one at the beginning and end of the input array and we calculate our current sum. if the current sum is equal to the target, we return the pair of indices added by one. if the current sum is bigger than our target, we decrement our right pointer. else we increment the left pointer.

            - Time Complexity: O(n) where n is the size of the input array. our two pointer approach starts at each end of the array and works towards the middle. 
            - Space Complexity: O(1) as the algorithm uses only a fixed amount of extra space for the two pointers (L and R).
        '''
        L, R = 0, len(nums) - 1

        while L < R:
            if nums[L] + nums[R] == target:
                return [L + 1, R + 1]
            elif nums[L] + nums[R] > target:
                R -= 1
            else:
                L += 1
solution = Solution()
print(solution.twoSum([2,7,11,15], 9))