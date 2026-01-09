## 3254. Find the Power of K-Size Subarrays I

'''
You are given an array of integers nums of length n and a positive integer k.

The power of an array is defined as:

Its maximum element if all of its elements are consecutive and sorted in ascending order.
-1 otherwise.
You need to find the power of all subarrays of nums of size k.

Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)].

 

Example 1:
Input: nums = [1,2,3,4,3,2,5], k = 3

Output: [3,4,-1,-1,-1]

Explanation:

There are 5 subarrays of nums of size 3:

[1, 2, 3] with the maximum element 3.
[2, 3, 4] with the maximum element 4.
[3, 4, 3] whose elements are not consecutive.
[4, 3, 2] whose elements are not sorted.
[3, 2, 5] whose elements are not consecutive.

Example 2:
Input: nums = [2,2,2,2,2], k = 4

Output: [-1,-1]

Example 3:
Input: nums = [3,2,3,2,3,2], k = 2

Output: [-1,3,-1,3,-1]
'''

class Solution:
    def resultsArray(self, nums: list[int], k:int) -> list[int]:
        '''
        1. Fixed Sliding Window
            - we iterate through our input using left and right pointers, our right pointer is going to keep going until the end of the array and our left pointer shifts when the window size exceeds size k. we also keep a separate variable called count which keeps track of the current consecutive count. when our window reaches size k and our count variable equals k, we append nums[r] to res. when our window exceeds size k, we shift our left pointer to the right. 
            - Time Complexity: O(n) where n is the length of the input array. this is because our right pointers keeps on going until the end of the array
            - Space Complexity: O(1) disregarding our output array because we are using a few variables to keep track our positioning in the array. 
        '''
        res = []

        L = 0

        for R in range(len(nums)):
            count = 1
            if R > 0 and nums[R] == nums[R - 1] + 1:
                count += 1
            while (R - L + 1) > k:
                if nums[L] + 1 == nums[L + 1]:
                    count -= 1
                L += 1
            while (R - L + 1) == k:
                res.append(nums[R] if count == k else -1)
        return res

solution = Solution()
print(solution.resultsArray([1,2,3,4,3,2,5], k=3))