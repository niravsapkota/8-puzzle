def manhattan_distance(board):
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Goal state configuration of the 8 Puzzle
    distance = 0
    
    for i in range(3):
        for j in range(3):
            value = board[i][j]
            if value != 0:
                
                #computes the row and column indices of the goal position for the current tile value by subtracting 1 from the tile value (to align the numbering starting from 0) and dividing by 3 to determine the row index and obtaining the remainder to find the column index
                goal_row, goal_col = divmod(value - 1, 3) 

                #calculates the Manhattan Distance for the current tile by taking the absolute differences between the current tile's position and goal position based on rows and columns
                distance += abs(i - goal_row) + abs(j - goal_col)  
    
    return distance


test_board = [
    [1, 5, 4],
    [2, 3, 8],
    [7, 6, 0]
]

distance = manhattan_distance(test_board)
print("Manhattan Distance:", distance)
