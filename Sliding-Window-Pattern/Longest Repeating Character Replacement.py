## 424. Longest Repeating Character Replacement

'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        1. hashmap + variable sliding window
            - we use two ptrs left and right to try out different sizes of windows that fit our criteria. we use a hashmap to count the occurrences of each character in our current substrings. we take the current length of substring and the max value of our hashmap, which represents the count of the most repeating character. we subtract the count from the length of the substring which represents how many replacements we can make. if the number of replacements is greater than k, then we have to shift our substring. 
            - Time Complexity: O(n) because our right ptr goes across to the end of the string
            - Space Complexity: O(n) because in the case that our whole string is a valid solution, our hashmap would be of size(n)
        '''

        count = {}

        L = res = 0 

        for R in range(len(s)):
            count[s[R]] = count.get(s[R], 0) + 1

            while (R - L + 1) - max(count.values()) > k:
                count[s[L]] -= 1
                L += 1
            res = max(res, (R - L + 1))
        return res

solution = Solution()
print(solution.characterReplacement("ABAB", k = 2))