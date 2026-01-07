## 713. Subarray Product Less Than K

'''
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

 

Example 1:
Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Example 2:
Input: nums = [1,2,3], k = 0
Output: 0
'''

class Solution:
    def subArrayLessThanK(self, nums: list[int], k: int) -> int:
        '''
        1. Variable Sliding Window
            - we want to the count of contiguous subarrays where the total product of the subarray is strictly less than k. we keep a running total of the product using a variable product. each time, we take the number at ptr r and multiply by the running product. if the running product is less than k, we take running total of subarrays and add our right ptr - left ptr + 1 to effectively add the new subarrays. if the product of the subarray is k or greater than k, we divide the number at the left ptr from the running product to remove it and shift the left ptr one to the right. 
                - Time Complexity: O(n) where n is the total length of nums and this is because our right ptr keep on incrementing to the end of the array.
                - Space Complexity: O(1) since we are not using any extra space in keping the total number of contiguous subarrays whose product are equal to or greater than k.
        '''
        if k == 0: return 0
        L = total = res = 0

        for R in range(len(nums)):
            total *= nums[R]
            while L <= R and total >= k:
                total = total // nums[L]
                L += 1
            res += (R - L + 1)
        return res

