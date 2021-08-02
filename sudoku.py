import math 
def solveSudoku(board,N):
    row=0
    col=0
    isUnsolved=False

    for i in range(N):
        for j in range(N):
            if(board[i][j]==0):
                row=i
                col=j
                isUnsolved=True
                break
        if(isUnsolved):
            break
    
    #noting to solve
    if(isUnsolved==False):
        return True
    
    for x in range(1,N+1):
        if(isValid(board,N,row,col,x)):
            board[row][col]=x
            if(solveSudoku(board,N)):
                return True
            else:
                board[row][col]=0
    #after replcing if still it is not true ,return false
    return False

        
def isValid(board,N,row,col,num):
    # row check
    for i in range(N):
        if(board[row][i]==num):
            return False
    # column check
    for i in range(N):
        if(board[i][col]==num):
            return False
    
    #same square
    square=int(math.sqrt(N))
    rowStart=row-row%square
    colStart=col-col%square
    for i in range(rowStart,rowStart+square):
        for j in range(colStart,colStart+square):
            if(board[i][j]==num):
                return False

    return True

def printSudoku(board,N):
    print("\n")
    print("##################soduku##################")
    print("\n")
    for i in range(N):
        print("\n")
        for j in range(N):
            print(board[i][j],end=" ")


def main():

        board=[
            [ 3, 0, 6, 5, 0, 8, 4, 0, 0 ],
            [ 5, 2, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 8, 7, 0, 0, 0, 0, 3, 1 ],
            [ 0, 0, 3, 0, 1, 0, 0, 8, 0 ],
            [ 9, 0, 0, 8, 6, 3, 0, 0, 5 ],
            [ 0, 5, 0, 0, 9, 0, 6, 0, 0 ],
            [ 1, 3, 0, 0, 0, 0, 2, 5, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 7, 4 ],
            [ 0, 0, 5, 2, 0, 6, 3, 0, 0 ]]
        N = len(board)
        print("N  :",N)
 
        if (solveSudoku(board, N)):
            printSudoku(board, N)
        else:
            print("No Solution")

main()            
