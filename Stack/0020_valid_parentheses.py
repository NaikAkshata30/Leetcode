# LeetCode 20 - Valid Parentheses
# Difficulty: Easy
# Topic: String, Stack
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def isValid(self, s):
        stack = []
        pair = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top != pair[c]:
                    return False 
        
        return len(stack)==0  