## 16. 3Sum Closest

'''
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
'''

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        '''
        1. Triple Nested for loop - Brute Force
            - using a triple nested for-loop to essentially go through every triplet, calculate the difference, and check if that
            is the minimum difference. 

            - Time Complexity: O(n ^ 3) where The outer loop runs approximately n times (where n is the length of nums). The middle loop runs roughly n-1 times for each iteration of the outer loop. The inner loop runs roughly n-2 times for each iteration of the middle loop.
            - Space Complexity: O(n) where The algorithm uses a constant amount of extra space. 
        '''

        '''
        2. Sorting + Two Pointer Approach (Converging)
            - we sort the array so that our smallest numbers occur at the beginning. set up two pointers and calculate the difference by adding
            the sum at those three indices and subtracting it from the target. if that difference is smaller than our current_difference, then update our current_difference. 
            - Time Complexity: O(n ^ 2) where n is the size of the input array. our outer loop runs about n times and for each iteration, our while loop runs approximated n times. sorting takes O(n log n) but here the nested for loop dominates
            - Space Complexity: O(1) aside from the space used to store the output. 
        '''
        res = 0
        min_diff = float('inf')
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L, R = i + 1, len(nums) - 1
            while L < R:
                currsum = nums[i] + nums[L] + nums[R]
                currdiff = abs(currsum - target)
                if currdiff < min_diff:
                    min_diff = currdiff
                    res = currsum
                if currsum > target:
                    R -= 1
                else:
                    L += 1
        return res
solution = Solution()
print(solution.threeSumClosest([-1,2,1,-4], 1))