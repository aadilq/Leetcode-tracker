## 80. Remove Duplicates from Sorted Array II

'''
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.


Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''

class Solution:
    def removeDuplicatesTwo(self, nums: list[int]) -> int:
        '''
        1. Two Pointer + Array Modification
            - we use a left and right pointer to scan through the array. with each number, count its current streak to check if the number appears at most once. If it does not, we use our left pointer to modify the array to the number does not appear more than twice. 
            - Time Complexity: O(n) because pointer R goes through the entire list, so it runs `n` times, where `n` is the length of `nums`.
            - Space Complexity: O(1) because we only use a few variables (`L`, `R`, `currentCount`, `i`) are used, which consume constant space.
        '''
        L = R = 0

        while R < len(nums):
            currentCount = 1
            while R + 1 < len(nums) and nums[R] == nums[R + 1]:
                currentCount += 1
                R += 1
            for i in range(min(2, currentCount)):
                nums[L] = nums[R]
                L += 1
            R += 1
        return L