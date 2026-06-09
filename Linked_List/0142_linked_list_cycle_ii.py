# LeetCode 142 - Linked List Cycle II
# Difficulty: Medium
# Topic: Hash Table, Linked List, Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        else:
            return None        

        fast = head

        while fast != slow:
            slow = slow.next
            fast = fast.next

        return slow       