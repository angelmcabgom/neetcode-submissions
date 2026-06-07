class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_arr = []

        for i, num in enumerate(nums):
            arr_wo_self = nums.copy()
            arr_wo_self.pop(i)

            current_product = 0
            for k, num_l in enumerate(arr_wo_self):
                if k == 0:
                    current_product = num_l
                else: 
                    current_product = current_product * num_l
            
            product_arr.append(current_product)


        return product_arr