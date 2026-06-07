class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        numsSet = set(nums)
        if not (len(numsSet) == len(nums)):
            return True
        return False
