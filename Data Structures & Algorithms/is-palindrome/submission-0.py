class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted = ''.join(filter(str.isalnum, s)).lower()
        lef, rig = 0, len(formatted) - 1

        while lef <= rig:
            if formatted[lef] == formatted[rig]:
                lef += 1 
                rig -= 1
            else:
                return False
        
        return True