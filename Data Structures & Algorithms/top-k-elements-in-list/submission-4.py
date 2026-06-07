class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_elements_map = {}

        for num in nums:
            occurences = top_elements_map.get(num, None)
            if occurences is not None:
                occurences = occurences + 1
                top_elements_map[num] = occurences
            else:
                top_elements_map[num] = 1
            
        arr = []

        for num, cnt in top_elements_map.items():
            arr.append([cnt, num])

        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
