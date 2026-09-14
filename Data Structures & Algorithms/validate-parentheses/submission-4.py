class Solution:
    def isValid(self, s: str) -> bool:
        bracketsMap = {"]": "[", "}": "{", ")": "("}
        stack = []

        for bracket in s:
            # if opener
            if bracket not in bracketsMap:
                stack.append(bracket)
            elif len(stack) == 0:  # closing bracket but stack empty
                return False
            elif bracketsMap[bracket] == stack[-1]:  # check top of stack
                stack.pop()
            else:
                return False

        return len(stack) == 0  # valid only if stack is empty