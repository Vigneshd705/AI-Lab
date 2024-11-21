def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9) 
    print()

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):  
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)): 
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, 'X'):  
        return 10 - depth
    if check_winner(board, 'O'): 
        return depth - 10
    if is_full(board): 
        return 0

    if is_maximizing:
        max_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ': 
                    board[i][j] = 'X'  
                    score = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    max_score = max(max_score, score)
                    alpha = max(alpha, score)
                    if beta <= alpha: 
                        return max_score
        return max_score

    else:
        min_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':  
                    board[i][j] = 'O'  
                    score = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' ' 
                    min_score = min(min_score, score)
                    beta = min(beta, score)
                    if beta <= alpha: 
                        return min_score
        return min_score

def find_best_move(board):
    best_score = float('-inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ': 
                score = minimax(board, 0, False, float('-inf'), float('inf'))
                    best_score = score
                    best_move = (i, j)
    return best_move

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        while True:
            move = input("Enter your move (row and column, 0-indexed, e.g., 0 1): ")
            try:
                row, col = map(int, move.split())
                    board[row][col] = 'O'
                    break
                else:
                    print("That cell is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Enter row and column as numbers (0-2).")

        print("\nYour Move:")
        print_board(board)

        if check_winner(board, 'O'):
            print("Congratulations, you win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        print("Computer's Turn:")
        best_move = find_best_move(board)
        if best_move:
            board[best_move[0]][best_move[1]] = 'X'

        print_board(board)

        if check_winner(board, 'X'):
            print("Computer wins! Better luck next time.")
            break
        if is_full(board):
            print("It's a draw!")
            break

play_tic_tac_toe()
