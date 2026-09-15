class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sqSets = {
            (0,0): set(),
            (0,1): set(),
            (0,2): set(),
            (1,0): set(),
            (1,1): set(),
            (1,2): set(),
            (2,0): set(),
            (2,1): set(),
            (2,2): set(),
        }
        cSets = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        rSets = [set(), set(), set(), set(), set(), set(), set(), set(), set()]


        for rowIndex, row in enumerate(board):
            cSet = cSets[rowIndex]

            for columnIndex, number in enumerate(row): 
                rSet = rSets[columnIndex]
                sqSetKey = (rowIndex // 3, columnIndex // 3)
                sqSet = sqSets.get(sqSetKey)
                # checking for columns and building rest of objects
                if number == '.':
                    continue
                elif number in cSet or number in rSet or number in sqSet:
                    return False
                else:
                    rSet.add(number)
                    cSet.add(number)
                    sqSet.add(number)


        return True  