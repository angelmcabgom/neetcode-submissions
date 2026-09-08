class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}

        for num in nums:
            if num in countMap:
                countMap[num] += 1
            else:
                countMap[num] = 1

        sortArr = []
        for num, count in countMap.items():
            # orders lexicographically which means it first compares the
            # the first element and then the second and so on
            sortArr.append([count, num])
        sortArr.sort()

        result = []

        while len(result) < k:
            result.append(sortArr.pop()[1])


        return result