## 977. Squares of a Sorted Array

'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
'''

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        '''
        1. Two Pointer Approach (Converging)
            - initialize two pointers at the beginning and end of the array. square both number at both pointers and compare. If the squared number at our left pointer is greater than the squared number at our right pointer, add the squared number at our left pointer and increment the left pointer. vice versa for the right pointer. The key is to add all of the greater squared number to the beginning of the array so we can return the reversed array, returning them into increasing order. 

            - Time Complexity: O(n) where n is the size of input array. This is because our two pointers start at the opposite ends of the array and converge towards the middle. After the while loop, reversing the array also takes O(n) time. 
            - Space Complexity: O(n) because our result list is going to n element requiring O(n) space
        '''

        res = []
        L, R = 0, len(nums) - 1

        while L <= R:
            if nums[L] ** 2 >= nums[R] ** 2:
                res.append(nums[L] ** 2)
                L += 1
            else:
                res.append(nums[R] ** 2)
                R -= 1
        return res[::-1]
solution = Solution()
print(solution.sortedSquares([[-4,-1,0,3,10]]))