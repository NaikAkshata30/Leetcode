# LeetCode 347 - Top K Frequent Elements
# Difficulty: Medium
# Topic: Array, Hash Table, Heap, Bucket Sort
# Time Complexity: O(n log n)
# Space Complexity: O(n)

class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        sort = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        result = []

        for i in range(k):
            result.append(sort[i][0])

        return result