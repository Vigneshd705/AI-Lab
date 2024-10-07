import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print()

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    
    return None

def is_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "X":
        return -10 + depth
    elif winner == "O":
        return 10 - depth
    elif is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player_turn = True  # Player is 'X', AI is 'O'
    
    while True:
        print_board(board)
        
        winner = check_winner(board)
        if winner or is_draw(board):
            break
        
        if player_turn:
            try:
                row = int(input("Enter row (0, 1, 2): "))
                col = int(input("Enter column (0, 1, 2): "))
                if row not in range(3) or col not in range(3):
                    print("Row and column must be 0, 1, or 2. Try again.")
                    continue
                if board[row][col] == " ":
                    board[row][col] = "X"
                    player_turn = False
                else:
                    print("Invalid move! Cell already occupied. Try again.")
            except ValueError:
                print("Invalid input! Please enter integers 0, 1, or 2.")
        else:
            move = best_move(board)
            if move:
                board[move[0]][move[1]] = "O"
                print(f"AI places 'O' at position ({move[0]}, {move[1]})")
                player_turn = True
            else:
                break
    
    print_board(board)
    winner = check_winner(board)
    if winner:
        if winner == "X":
            print("X wins!")
        else:
            print("O wins!")
    else:
        print("It's a draw!")

play_game()