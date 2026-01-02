## 151. Reverse Words in a String

'''
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
'''

class Solution:
    def reverseStringsWord(self, s: str) -> str:
        '''
        1. Two Pointer + String Reversal
            - in python string data type is not mutable so we cannot solve this using O(1) space. instead we can split our string into a list so that each word is in a list. then we iterate through each word backwards and append it into our result list and between each word, we append a space. 
            - Time Complexity: O(n) where n is the number of words in the input string. this is because we go through each word and convert it into a list. then we iterate backwards through the list of words and append it our resulting list, which we convert back into a string.
            - Space Complexity: O(n) where n is the number of words in the input string. this is because our result list will be as big as our input string. 
        '''

        words = s.split()
        res = []

        for i in range(len(words) - 1, -1, -1):
            res.append(words[i])
            if i != 0:
                res.append(" ")
        return "".join(res)
solution = Solution()
print(solution.reverseStringsWord("the sky is blue"))