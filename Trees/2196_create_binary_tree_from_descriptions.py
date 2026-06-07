# LeetCode 2196 - Create Binary Tree From Descriptions
# Difficulty: Medium
# Topic: Tree, Hash Table, Binary Tree
# Daily Question: Yes
# Time Complexity: O(n)
# Space Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        mp = {}
        child_set = set()

        for parent, child, isleft in descriptions:
            if parent not in mp:
                mp[parent] = TreeNode(parent)

            if child not in mp:
                mp[child] = TreeNode(child)

            if isleft == 1:
                mp[parent].left = mp[child]
            else:
                mp[parent].right = mp[child]

            child_set.add(child)

        for parent, child, isleft in descriptions:
            if parent in child_set:
                continue
            else:
                return mp[parent]