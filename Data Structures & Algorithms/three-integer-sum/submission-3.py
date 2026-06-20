class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        sorted_arr = sorted(nums)

        for i, num in enumerate(sorted_arr):
            if i > 0 and num == sorted_arr[i - 1]:
                continue

            lef, rig = i + 1, len(sorted_arr) - 1
            tgt = -num 

            while lef < rig:
                curr_sum = sorted_arr[lef] + sorted_arr[rig]
                
                if curr_sum == tgt:
                    triplets.append([num, sorted_arr[lef], sorted_arr[rig]])
                    lef += 1
                    rig -= 1
                    while lef < rig and sorted_arr[lef] == sorted_arr[lef - 1]:
                        lef += 1
                    while lef < rig and sorted_arr[rig] == sorted_arr[rig + 1]:
                        rig -= 1
                elif curr_sum < tgt:
                    lef += 1
                else:
                    rig -= 1 

        return triplets