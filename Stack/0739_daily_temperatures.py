# LeetCode 739 - Daily Temperatures
# Difficulty: Medium
# Topic: Array, Stack, Monotonic Stack
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        output = [0] * n

        for i,t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stack_t,stack_i = stack.pop()
                output [stack_i] = i - stack_i
            stack.append((t, i))

        return output        