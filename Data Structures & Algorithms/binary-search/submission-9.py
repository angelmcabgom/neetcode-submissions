class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lef, rig = 0, len(nums)

        while lef < rig:

            mid = (lef + rig) // 2 


            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lef = lef + 1
            else:
                rig = rig - 1 
        

        
        return -1