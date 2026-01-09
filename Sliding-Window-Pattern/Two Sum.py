## 1. Two Sum

'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        '''
        1. Hashmap + complement approach
            - to achieve a linear time solution, we can go through each index and number in nums, calculate the complement of the number by subtracting the current number from the target, if that number exists within our hashmap, then we can the return index of the complement along with the current number. if the complement does not exist, we add our current number to the hashmap where the number is the key and index is the value. 
            - Time Complexity: O(n) where n is the length of the nums array. this is because we do one pass through find the complement of each number.
            - Space Complexity: O(n) because we are populating each number from nums into our hashmap and since our nums array can only have unique values, our hashmap is bound to be as big as our nums array.
        '''

        count = {}

        for i, num in enumerate(nums):
            if target - num in count:
                return [count[target - num], i]
            count[num] = i
solution = Solution()
print(solution.twoSum([2,7,11,15], target=9))