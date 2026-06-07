# LeetCode 1323 - Maximum 69 Number
# Difficulty: Easy
# Topic: Math, Greedy
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def maximum69Number (self, num):
        num = list(str(num))

        for i in range(len(num)):
            if num[i] == "6":
                num[i] = "9"
                break
        return int("".join(num))