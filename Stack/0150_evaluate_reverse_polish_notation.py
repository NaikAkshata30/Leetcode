# LeetCode 150 - Evaluate Reverse Polish Notation
# Difficulty: Medium
# Topic: Array, Math, Stack
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = {'+', '-', '*', '/'}

        for ch in tokens:
            if ch not in operator:
                stack.append(int(ch))
            else:
                b = stack.pop()
                a = stack.pop()

                if ch == '+':
                    stack.append(a+b)
                elif ch == '-':
                    stack.append(a-b)
                elif ch == '*':
                    stack.append(a*b)
                else:
                    stack.append(int(a / b)) 

        return stack.pop()                  