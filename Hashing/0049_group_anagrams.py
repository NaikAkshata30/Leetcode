# LeetCode 49 - Group Anagrams
# Difficulty: Medium
# Topic: Array, Hash Table, String, Sorting
# Time Complexity: O(n * k log k)
# Space Complexity: O(n)

class Solution(object):
    def groupAnagrams(self, strs):
        group = {}

        for word in strs:
            key = ''.join(sorted(word))

            if key not in group:
                group[key] = []

            group[key].append(word)

        return list(group.values())