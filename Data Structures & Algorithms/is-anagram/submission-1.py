class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not (len(s) == len(t)):
            return False

        charCount = {}  # init hash map

        for char in s:
            charCount[char] = charCount.get(char, 0) + 1 # return key value or default in this case 0
            
        for char in t:
            if char not in charCount or charCount[char] == 0: 
                # check if inside hash map or substract until 0, check if already used all occurences
                # so if current iteration chart tries to be matched and substracted function ends
                return False
            charCount[char] -= 1
            
        return True
        
        