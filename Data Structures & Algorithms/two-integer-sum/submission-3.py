class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i, num in enumerate(nums):
            tgt_diff = target - num
            diff_index = hm.get(tgt_diff, -1)

            if diff_index != -1:
                return [diff_index, i]
            else: 
                hm[num] = i
