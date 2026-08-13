class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for arr in matrix:
            lef, rig = 0, len(arr)

            while lef < rig: 
                mid = (lef + rig) // 2
                if arr[mid] == target:
                    return True 
                elif arr[mid] < target:
                    lef = mid + 1
                else: 
                    rig = mid
        
        return False
