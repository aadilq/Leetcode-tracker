## 15. 3Sum

'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]

Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.

The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
'''

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        '''
        1. Sorting + Two Pointer Approach (Converging)
            - we sort the array in order to eliminate adjacent numbers that are the same as to eliminate duplicate triplets. We use a two pointer approach to find our triplet of numbers which added together, equal to 0.
            
            - Time Complexity: O(n ^ 2) because the outer loop runs approximately n times and for each iteration, the inner while loop uses the two-pointer approach to scan through the remaining elements, which in the worst case also takes linear time. Initial sorting step take O(n log n) but in this case the nested loops dominate
            - Space Complexity: O(1) aside from the space used to store the output. 
        '''

        res = []

        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L, R = i + 1, len(nums) - 1
            while L < R:
                currentSum = nums[i] + nums[L] + nums[R]
                if currentSum > 0:
                    R -= 1
                elif currentSum < 0:
                    L += 1
                else:
                    res.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
        return res
solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4]))
                    

