class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lef, rig = 0, len(numbers) - 1

        while lef < rig:
            if numbers[lef] + numbers[rig] == target:
                return [lef + 1, rig + 1]
            elif numbers[lef] + numbers[rig] < target:
                lef += 1
            else:
                rig -= 1