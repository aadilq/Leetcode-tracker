## 259. 3Sum Smaller

'''
Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Example1

Input:  nums = [-2,0,1,3], target = 2
Output: 2
Explanation:
Because there are two triplets which sums are less than 2:
[-2, 0, 1]
[-2, 0, 3]

Example2

Input: nums = [-2,0,-1,3], target = 2
Output: 3
Explanation:
Because there are three triplets which sums are less than 2:
[-2, 0, -1]
[-2, 0, 3]
[-2, -1, 3]

'''

class Solution:
    def threeSumSmaller(self, nums: list[int], target: int) -> list[int]:
        '''
        1. Sorting + Two Pointer Approach(Converging)
            - We sort the array and use a two pointer converging approach to find triplets whose sum is less than the target. if we find a sum that is less than the target, we know the everything from our left to right pointer is valid so we add to res 
            - Time Complexity: O(n ^ 2) where n is the size of the input array. our outer loop runs about n times and for each iteration, our while loop runs approximated n times. sorting takes O(n log n) but here the nested for loop dominates
            - Space Complexity: O(1) aside from the space used to store the output. 
        '''
        nums.sort()

        res = 0 

        for i in range(len(nums) - 2):
            L, R = i + 1, len(nums) - 1
            while L < R:
                currsum = nums[i] + nums[L] + nums[R]
                if currsum < target:
                    res += R - L
                    L += 1
                else:
                    R -= 1
        return res
solution = Solution()
print(solution.threeSumSmaller([-2,0,1,3], 2))