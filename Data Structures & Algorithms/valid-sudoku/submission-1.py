class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        
        seen_in_col = {i: set() for i in range(9)}
        seen_in_boxes = {
            (r, c): set()
            for r in range(3)
            for c in range(3)
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


            