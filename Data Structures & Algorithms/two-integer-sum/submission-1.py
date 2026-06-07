class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]: # guaranteed to always have a solution
        seen = {} # hash map
        for i, num in enumerate(nums): # get index and num
            diff = target - num # get diff var
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i # add to see 

print(Solution().twoSum([5, 5], 10))