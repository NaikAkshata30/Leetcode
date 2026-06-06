# LeetCode 2574 - Left and Right Sum Differences
# Difficulty: Easy
# Topic: Prefix Sum
# Daily Question: Yes
# Date Solved: 2026-06-06
# Time Complexity: O(n)
# Space Complexity: O(1) excluding output array

from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        sum_of_elements = sum(nums)
        curr = 0
        result = []

        for num in nums:
            left_sum = curr
            curr += num

            right_sum = sum_of_elements - curr

            res = abs(left_sum - right_sum)

            result.append(res)

        return result