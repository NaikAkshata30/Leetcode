# LeetCode 238 - Product of Array Except Self
# Difficulty: Medium
# Topic: Array, Prefix Sum
# Time Complexity: O(n)
# Space Complexity: O(1) excluding output array

class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        product = 1
        for i in range(n):
            answer[i] = product
            product = product * nums[i]


        product = 1
        for i in range(n-1, -1, -1):
            answer[i] = answer[i] * product
            product = product * nums[i]    
        
        return answer    