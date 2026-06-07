class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {} # dict with arr indices
        arr = [] # result arr
        i = 0


        for str in strs:
            sorted_str = ''.join(sorted(str))
            sub_arr_i = hm.get(sorted_str, None)

            if sub_arr_i is not None:
                # push into subarr
                arr[sub_arr_i].append(str)
            else: 
                arr.append([str])
                hm[sorted_str] = i
                i = i + 1

        return arr