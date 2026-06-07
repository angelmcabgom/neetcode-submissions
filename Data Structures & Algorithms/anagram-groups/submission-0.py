class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # hash map

        for str in strs:
            count = [0] * 26 # init a list with 26 int in this case 0

            for char in str:
                count[ord(char) - ord('a')] += 1 # create the unique key array for the anagram will be used to create the hashmap entry

            res[tuple(count)].append(str)
        
        return list(res.values())