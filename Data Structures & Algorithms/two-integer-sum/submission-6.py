class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numSet = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in numSet:
                return [numSet[diff], i]
            else:
                numSet[num] = i 