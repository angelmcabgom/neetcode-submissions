class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashFrequency = {}

        for num in nums:
            hashFrequency[num] = hashFrequency.get(num, 0) + 1

        sortedHashFrequency = sorted(hashFrequency, reverse=True, key=hashFrequency.get)

        topFrequent = []

        i = 0
        while k > 0:
            topFrequent.append(sortedHashFrequency[i])
            i += 1
            k -= 1

        return topFrequent