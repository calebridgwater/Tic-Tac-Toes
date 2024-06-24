import tkinter as tk
from tkinter import messagebox

# initialize the main game window
root = tk.Tk()
root.title("Tic-Tac-Toe from Caleb")

# Creates the tic-tac-toe board
board = [None] * 9
current_player = "x"

# Create buttons for the Tic-Tac-Toe board
buttons = []
for i in range(9):
    button = tk.Button(root, text="", font="Helvetica 20", width=5, height=2, command=lambda

i=i: click(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

def check_winner():
    # check all possible winning combinations
    combinations = [
        # Row combinations-
        (0, 1, 2,), (3, 4, 5), (6, 7, 8),
        # Column combinaitons- 
        (0, 3, 6), (1, 4, 7), (2, 5, 8), 
        # Diagonal combinations-
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in combinations:
        if board[a] == board[b] == board[c] and board[a] is not None:
            return board[a] 
    return None

def click(
    button: any, 
    index: any):
    global current_player
    if board[index] is None:
        board[index] = current_player
    
def reset_game():
    global board, current_player
    board = [None] * 9
    current_player = "X"
    for button in buttons:
        button.config(text="",state=tk.NORMAL)
        
button.config(text=current_player, state=tk.DISABLED)
winner = check_winner()
if winner:        
    messagebox.showinfo("Tic-Tac-Toe", f"Player {winner} wins!")
    reset_game()
elif all(board):
        
    messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
    reset_game()
else:
    current_player = "0" if current_player == "X" else "x"      

# Start the main loop
root.mainloop()  