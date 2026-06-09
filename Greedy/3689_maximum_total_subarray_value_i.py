# LeetCode 3689 - Maximum Total Subarray Value I
# Difficulty: Medium
# Topic: Array, Greedy
# Daily Question: Yes
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        
        maximum = max(nums)
        minimum = min(nums)
        
        return (maximum - minimum) * k