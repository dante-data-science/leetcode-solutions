class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        flag = True
        seen1 = set()
        seen2 = set()
        seen3 = set()
        tiles = [0] * 9
        columns = [0] * 9
        
        for j in range(0, 9, 3):
            tile1 = []
            tile2 = []
            tile3 = []
            for i in range(3):
                tile1.extend(board[i + j][:3])
                tile2.extend(board[i + j][3:6])
                tile3.extend(board[i + j][6:9])

            tiles[j] = tile1
            tiles[j + 1] = tile2
            tiles[j + 2] = tile3

        for i in range(9):
            column = [0] * 9
            for j in range(9):
                column[j] = board[j][i]         
            columns[i] = column
        for i in range(9):
            row = board[i]
            column = columns[i]
            tile = tiles[i]
            seen1 = set()
            seen2 = set()
            seen3 = set()
            for item in row:
                if item != '.' and item in seen1:
                    flag = False
                seen1.add(item)
            for j in range(9):
                if column[j] != '.' and column[j] in seen2:
                    flag = False
                seen2.add(column[j])
            for j in range(9):
                if tile[j] != '.' and tile[j] in seen3:
                    flag = False
                seen3.add(tile[j])
       
        return(flag)
        