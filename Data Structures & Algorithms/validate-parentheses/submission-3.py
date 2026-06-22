class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        chars_dict = {"{": "}", "[": "]", "(": ")"}
        stack = []

        for char in s:
            if char in chars_dict:
                stack.append(char)
            else:
                if not stack or chars_dict[stack.pop()] != char:
                    return False
        
        return not stack

        return True