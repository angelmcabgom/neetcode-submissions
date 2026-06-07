class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        noDupes = set(nums)

        if len(noDupes) < len(nums):
            return True
        
        return False
    