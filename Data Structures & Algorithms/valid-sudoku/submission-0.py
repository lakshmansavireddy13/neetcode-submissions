class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows={}
        cols={}
        boxes={}

        for i in range(9):
            for j in range(9):
                if board[i][j] =='.':
                    continue
                
                num=board[i][j]

                if i not in rows:
                    rows[i]=set()

                if j not in cols:
                    cols[j]=set()
                
                box=(i//3,j//3)

                if box not in boxes:
                    boxes[box]=set()
                
                if num in rows[i]:
                    return False
                
                if num in cols[j]:
                    return False
                
                if num in boxes[box]:
                    return False
                
                rows[i].add(num)
                cols[j].add(num)
                boxes[box].add(num)
            
        return True
                
                
