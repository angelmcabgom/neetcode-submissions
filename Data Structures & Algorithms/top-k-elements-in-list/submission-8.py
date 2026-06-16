class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_freq = {}

        for num in nums:
            entry = top_freq.get(num, None)

            if entry is not None:
                top_freq[num] += 1
            else:
                top_freq[num] = 1

        top_freq_arr = []
        for number, cnt in top_freq.items():
            top_freq_arr.append([cnt, number]) 
        
        top_freq_arr.sort()

        res = []
        while len(res) < k:
            res.append(top_freq_arr.pop()[1]) 
        
        return res
