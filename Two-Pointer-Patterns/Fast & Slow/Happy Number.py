## 202. Happy Number

'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Example 2:

Input: n = 2
Output: false
'''

class Solution:
    def happyNumber(self, n: int) -> bool:
        '''
        1. Fast & Slow pointer approach
            - we use a fast and slow pointer approach to square each number with the slow pointer squaring the number once and the fast pointer squaring the numbe twice. if there two pointers meet and the number that they meet at is not 1, then this means that number is not happy otherwise if they do meet at one, it means that they are happy. 

            19 -> 82 -> 68 -> 100 -> 1
             S
             F

            - Time Complexity: O(n) where n is the number of nodes that our fast and slow pointer will traverse through in an endless cycle 
            - Space Complexity: O(1) since we are not using any additional data structures
        '''
        slow = fast = n

        while True:
            slow = self.findSquare(slow)
            fast = self.findSquare(self.findSquare(fast))
            if slow == fast:
                break
        return slow == 1

    def findSquare(self, n: int) -> int:
        output = 0
        while n > 0:
            digit = n % 10
            output += digit ** 2
            n = n // 10
        return output

solution = Solution()
print(solution.happyNumber(19))
