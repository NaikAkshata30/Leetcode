# LeetCode 217 - Contains Duplicate
# Difficulty: Easy
# Topic: Array, Hash Table
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def containsDuplicate(self, nums):

        n = len(nums)
        unique_numbers = len(set(nums))

        if n != unique_numbers:
            return True

        return False