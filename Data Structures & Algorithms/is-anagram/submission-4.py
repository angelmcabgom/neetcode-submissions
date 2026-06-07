class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hm_s = {}
        hm_t = {}

        for i, char in enumerate(s):
            hm_s[char] = hm_s.get(char, 0) + 1
            hm_t[t[i]] = hm_t.get(t[i], 0) + 1

        if hm_t == hm_s:
            return True

        return False