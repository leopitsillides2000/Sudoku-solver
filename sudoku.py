import sys
sys.setrecursionlimit(10**9)

test_grid = [
    [6,0,0,0,0,0,5,3,0],
    [0,0,0,0,0,2,7,0,0],
    [5,0,7,0,9,6,0,1,8],
    [0,0,6,0,0,1,0,8,0],
    [0,9,8,0,0,0,0,0,0],
    [0,0,0,0,2,0,0,0,0],
    [0,0,0,0,0,0,9,0,0],
    [0,0,0,2,0,0,0,4,3],
    [3,1,0,0,0,9,0,6,2],
    ]

def board(bo):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print('----------------------')
        for j in range(9):
            if (j + 1) % 3 == 0 and j != 8:
                print(bo[i][j], end = ' | ')
            else:
                print(bo[i][j], end = ' ')
        print()  

def subGrid(grid, row, col):
    ans = []
    for i in range(3*(int(row/3)), 3*(int(row/3) + 1)):
        for j in range(3*(int(col/3)), 3*(int(col/3) + 1)):
            ans.append(grid[i][j])
    return ans
    
def valid(grid, row, col):
    
    if grid[row].count(grid[row][col]) > 1:
        return False
        
    if list(zip(*grid))[col].count(grid[row][col]) > 1:
        return False
        
    if subGrid(grid, row, col).count(grid[row][col]) > 1:
        return False
    
    return True

store = []
rowNum = 0
colNum = 0

def solver(startGrid):

    global rowNum
    global colNum
    
    while rowNum <= 8 and colNum <= 8:
        
        if [rowNum, colNum] in store:
            startGrid[rowNum][colNum] += 1
        
        if startGrid[rowNum][colNum] == 0:
            store.append([rowNum, colNum])
            startGrid[rowNum][colNum] += 1
        
        while valid(startGrid, rowNum, colNum) == False:
            startGrid[rowNum][colNum] += 1
            if startGrid[rowNum][colNum] == 10:
                break
        
        if startGrid[rowNum][colNum] == 10:
            del store[-1]
            startGrid[rowNum][colNum] = 0
            [rowNum, colNum] = store[-1]
            return solver(startGrid)
        else:
            if colNum == 8:
                colNum = 0
                rowNum += 1
            else:
                colNum += 1
    
    return board(startGrid)

print(solver(test_grid))