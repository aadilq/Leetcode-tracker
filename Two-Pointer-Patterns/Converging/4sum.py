## 18. 4Sum

'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
'''

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[int]:
        '''
        1. Sorting + Two Pointer Approach (Converging)
            - we sort the array so that elements are in increasing order. since we want quadruplets that equal the target, we can use two for loops that get our first two numbers and a left and right pointer to get our last two pointers. 
            - Time Complexity: The outer two loops run approximately O(n^2) times. For each pair (i, j), the two-pointer search runs in O(n) time. Overall, the nested loops combined with the two-pointer approach result in a time complexity of O(n^3).
            - Space Complexity:  auxiliary space used for storing the result is proportional to the number of quadruplets found, which in the worst case can be O(n^4)
        '''
        nums.sort()

        res = []

        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > 0 and nums[j] == nums[j - 1]:
                    continue
                L, R = j+1, len(nums) - 1
                while L < R:
                    currsum = nums[i] + nums[j] + nums[L] + nums[R]
                    if currsum > target:
                        R -= 1
                    elif currsum < target:
                        L += 1
                    else:
                        res.append([nums[i], nums[j], nums[L], nums[R]])
                        L += 1
                        R -= 1
                        while L < R and nums[L] == nums[L - 1]:
                            L += 1
        return res

solution = Solution()
print(solution.fourSum([1,0,-1,0,-2,2], target=0))
        