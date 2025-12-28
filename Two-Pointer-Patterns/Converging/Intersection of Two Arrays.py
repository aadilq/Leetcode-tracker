## 349. Intersection of Two Arrays

'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
'''

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        '''
        1. Hashset Approach
            - convert nums1 into a set so that all duplicates are removed. go through each number in nums2. if the number exist in the nums1 set, add
            it to our resulting list and remove that number from the nums1 set.

            - Time Complexity: O(n) for converting the nums1 into a set and O(n) for going through each number in nums2. 
            - Space Complexity: O(n) because the size our set depends on the number of unique numbers in nums1
        '''
        seen = set(nums1)

        res = []

        for num in nums2:
            if num in seen:
                res.append(num)
                seen.remove(num)
        return res

solution = Solution()
print(solution.intersection([1,2,2,1], [2,2]))