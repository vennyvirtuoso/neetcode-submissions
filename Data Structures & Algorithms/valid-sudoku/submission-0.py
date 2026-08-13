class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subbox = [[set() for _ in range(3)] for _ in range(3)]
        # print(subbox)
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                if board[i][j] in rows[i]:
                    return False
                else:
                    rows[i].add(board[i][j])

                if board[i][j] in cols[j]:
                    return False
                else:
                    cols[j].add(board[i][j])
                
                boxi = i//3
                boxj=j//3
                if board[i][j] in subbox[boxi][boxj]:
                    return False
                else:
                    subbox[boxi][boxj].add(board[i][j])
        # print(subbox)
        return True