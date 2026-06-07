# LeetCode 242 - Valid Anagram
# Difficulty: Easy
# Topic: Hash Table, String, Sorting
# Time Complexity: O(n log n)
# Space Complexity: O(n)

class Solution(object):
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)