# LeetCode 2161 - Partition Array According to Given Pivot
# Difficulty: Medium
# Topic: Array, Two Pointers, Simulation
# Daily Question: Yes
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_num = []
        equal_num = []
        greater_num = []

        for i in nums:
            if i < pivot:
                less_num.append(i)
            elif i == pivot:
                equal_num.append(i)
            else:
                greater_num.append(i)

        return less_num + equal_num + greater_num
            