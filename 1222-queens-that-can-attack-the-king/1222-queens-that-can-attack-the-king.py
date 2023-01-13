class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        table=set(tuple(i) for i in queens)
        good_queens=self.find_nearest_queens(king[0],king[1],table)
        directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
        x_int=king[0]
        y_int=king[1]
        result=[]
        for dx,dy in directions:
            for i in range(1,8):
                    x=x_int + i*dx
                    y=y_int + i*dy
                    if (0<=x<=7 and 0<=y<=7) and (x,y) in table:
                        result.append((x,y))
                        break

        return result

    def find_nearest_queens(self,king_row,king_col,table):
        good_queens =set()
        #left
        for i in range(king_col-1,-1,-1):
            if (king_row,i) in table:
                good_queens.add((king_row,i))
                break
        #right
        for i in range(king_col+1,8):
            if (king_row,i) in table:
                good_queens.add((king_row,i))
                break
        #up
        for i in range(king_row-1,-1,-1):
            if (i,king_col) in table:
                good_queens.add((i,king_col))
                break
        #down
        for i in range(king_row+1,8):
            if (i,king_col) in table:
                good_queens.add((i,king_col))
                break
    
        #left_up
        r=king_row - 1
        c=king_col - 1
        while r>=0 or c>=0:
            if (r,c) in table:
                good_queens.add((r,c))
                break
            r-=1
            c-=1

        #right_up
        r=king_row - 1
        c=king_col + 1
        while r>=0 or c<=7:
            if (r,c) in table:
                good_queens.add((r,c))
                break
            r-=1
            c+=1

        #left_down
        r=king_row + 1
        c=king_col - 1
        while r<=7 or c>=0:
            if (r,c) in table:
                good_queens.add((r,c))
                break
            r+=1
            c-=1
        
        #right_down
        r=king_row + 1
        c=king_col + 1
        while r<=7 or c<=7:
            if (r,c) in table:
                good_queens.add((r,c))
                break
            r+=1
            c+=1
    
        return good_queens        
