class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_elements_map = {}

        for num in nums:
            if num in top_elements_map:
                top_elements_map[num] += 1 
            else:
                top_elements_map[num] = 1
        
        top_el_arr = []
        for num, cnt in top_elements_map.items():
            top_el_arr.append([cnt, num])
        top_el_arr.sort() 


        res = []
        while len(res) < k:
            res.append(top_el_arr.pop()[1])
               
        return res
