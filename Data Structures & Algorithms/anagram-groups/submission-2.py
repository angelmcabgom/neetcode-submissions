class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strHashMap = {}

        for str in strs:
            sortedStr = "".join(sorted(str))

            if sortedStr in strHashMap:
                strHashMap[sortedStr].append(str)
            else:
                strHashMap[sortedStr] = [str]

        outputArr = []
        for groupedAnagrams in strHashMap.values():
            outputArr.append(groupedAnagrams)

        return outputArr
