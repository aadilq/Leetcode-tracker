## 219. Contains Duplicate II

'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''
class Solution:
    def containsDuplicateII(self, nums: list[int], k:int) -> bool:
        '''
        1. Variable sliding window
            - since are want to check for duplicate numbers, we can use a set to do so and to make the indices i and j are less than k, we can use a sliding window. we use left and right ptrs to iterate through the array. when our sliding window goes out of bounds, greater than k, we shift our left ptr and remove the number at our left ptr from the set. if our window is in bounds and the numbers match, we return true
            - Time Complexity: O(n) where n is the length of the input array. this is because our right ptr moves across through the whole array. 
            - Space Complexity: O(n) because in the worst case, our set could also be the same size as our input array
        '''

        Set = set()

        L = 0 

        for R in range(len(nums)):
            if (R - L) > k:
                Set.remove(nums[L])
                L += 1
            if nums[R] in Set:
                return True
            Set.add(nums[R])
        return False

solution = Solution()
print(solution.containsDuplicateII([1,2,3,1], k = 3))
print(solution.containsDuplicateII([1,0,1,1], k = 1))
print(solution.containsDuplicateII([1,2,3,1,2,3], k = 2))