# LeetCode 141 - Linked List Cycle
# Difficulty: Easy
# Topic: Hash Table, Linked List, Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        curr = head 

        while curr:
            if curr in seen:
                return True
            seen.add(curr)    
            curr = curr.next

        return False        