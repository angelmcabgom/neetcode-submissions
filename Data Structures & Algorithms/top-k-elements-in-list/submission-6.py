class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_freq = {}

        for num in nums:
            if num not in top_freq:
                top_freq[num] = 1
            else:
                top_freq[num] += 1


        arr = []
        print(top_freq)
        for num, cnt in top_freq.items(): # {1: 3, 2: 2, 3: 1}
            arr.append([cnt, num])

        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res