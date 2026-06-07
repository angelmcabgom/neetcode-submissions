class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i, num in enumerate(nums):
            tgt_diff = target - num
            chk_element_i = hm.get(tgt_diff, None)

            if chk_element_i is not None:
                return [chk_element_i, i]
            else:
                hm[num] = i