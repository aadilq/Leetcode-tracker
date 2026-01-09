## 3. Longest Substring Without Repeating Characters

'''
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        1. Variable Sliding Window
            - to find the length of the longest substring without repeating characters, we can use a variable sliding window. we're going to use a hashset to keep track of the current characters that we have seen so far. when we come across a character that is already in our hashset, we keep on shifting our left pointer until that character is not seen in the hashset anymore. 
            - Time Complexity: O(n) where n is the length of the string because our right pointer is going to keep on moving until the end of the string. 
            - Space Complexity: O(n) where n is the length of the string because in the worst case, all the character in our string are unique and our hashset is the same size of the length of the string. 
        '''

        Set = set()

        L = res = 0 


        for R in range(len(s)):
            while s[R] in Set:
                Set.remove(s[L])
                L += 1
            Set.add(s[R])
            res = max(res, (R - L + 1))
        return res
solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))
