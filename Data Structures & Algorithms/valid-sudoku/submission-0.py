class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen=set()
            for j in range(9):
                if board[i][j]!='.':
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        
        for j in range(9):
            seen=set()
            for i in range(9):
                if board[i][j]!='.':
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        
        for br in range(0,9,3):
            for bc in range(0,9,3):
                seen=set()

                for i in range(br,br+3):
                    for j in range(bc,bc+3):
                        if board[i][j]!='.':
                            if board[i][j] in seen:
                                return False
                            seen.add(board[i][j])
        return True

                
                    
        