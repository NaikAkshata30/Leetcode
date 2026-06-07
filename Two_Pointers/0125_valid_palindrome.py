# LeetCode 125 - Valid Palindrome
# Difficulty: Easy
# Topic: Two Pointers, String
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def isPalindrome(self, s):
        new_string = ""
        
        for char in s: 
            if char.isalnum(): 
                new_string += char.lower()

        return new_string == new_string[::-1]        