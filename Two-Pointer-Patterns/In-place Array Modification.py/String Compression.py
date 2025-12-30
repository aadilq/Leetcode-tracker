## 443. String Compression

'''
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Note: The characters in the array beyond the returned length do not matter and should be ignored.

 

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.

Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
'''

class Solution:
    def stringCompression(self, chars: list[str]) -> int:
        '''
        1. Two Pointers + Array Modification
            - we use two pointers to keep track of how many each character exists. our right pointer counts how many of each exist and our left pointer is going to rewrite the rest of the array based off of how many of each character we have. at the end, we return our left pointer
            - Time Complexity: O(n) where n is the length of the char array. this is because our right pointer iterates throughout the length of our input array
            - Space Complexity: O(1) since the algorithm uses only a few extra variables (readptr, writeptr, current_char, count, stringCount, and a temporary loop variable)

            ["a","a","a","b","b","c","c","c"]
                         rp
                  wp
        '''

        read_ptr = write_ptr = 0

        while read_ptr < len(chars):
            currentCount = 1
            current_char = chars[read_ptr]
            while read_ptr + 1 < len(chars) and current_char == chars[read_ptr]:
                read_ptr += 1
                currentCount += 1
            chars[write_ptr] = current_char
            write_ptr += 1
            if currentCount > 1:
                str_count = str(currentCount)
                for char in str_count:
                    chars[write_ptr] = char
                    write_ptr += 1
                read_ptr += 1
        return write_ptr

solution = Solution()
print(solution.stringCompression(["a","a","b","b","c","c","c"]))
            

            


