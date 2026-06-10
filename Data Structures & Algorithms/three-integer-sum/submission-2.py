class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i, num in enumerate(nums):
            # not first of the array and if it is the same element as before we dont wanna use the same value twice
            if i > 0 and num == nums[i - 1]:
                continue

            lef, rig = i + 1, len(nums) - 1
             

            while lef < rig:
                dreiSum = num + nums[lef] + nums[rig]

                if dreiSum > 0:
                    rig -= 1
                elif dreiSum < 0:
                    lef += 1 
                else: 
                    triplets.append([num, nums[lef], nums[rig]])
                    lef += 1 
                    while nums[lef] == nums[lef - 1] and lef < rig:
                        lef += 1 
                    

        return triplets