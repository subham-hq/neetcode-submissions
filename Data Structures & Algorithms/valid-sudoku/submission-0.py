class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        
        seen_in_col = {
            0: set(),
            1: set(),
            2: set(),
            3: set(),
            4: set(),
            5: set(),
            6: set(),
            7: set(),
            8: set(),
        }
        seen_in_boxes = {
            (0, 0): set(),
            (0, 1): set(),
            (0, 2): set(),
            (1, 0): set(),
            (1, 1): set(),
            (1, 2): set(),
            (2, 0): set(),
            (2, 1): set(),
            (2, 2): set(),
        }

        for i in range(9):
            seen_in_row = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue

                # check rows
                if board[i][j] in seen_in_row:
                    return False
                seen_in_row.add(board[i][j])

                # check columns
                if board[i][j] in seen_in_col[j]:
                    return False
                seen_in_col[j].add(board[i][j])

                # check boxes
                box = (i // 3, j // 3)
                if board[i][j] in seen_in_boxes[box]:
                    return False
                seen_in_boxes[box].add(board[i][j])

        return True


            