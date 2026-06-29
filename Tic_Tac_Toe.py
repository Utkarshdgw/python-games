print (" 1 | 2 | 3 ")
print (" ---------- ")
print (" 4 | 5 | 6 ")
print (" ---------- ")
print (" 7 | 8 | 9 ")

turn = "X"

board = ["1","2","3",
         "4","5","6",
         "7","8","9"]
while True:
    position = (int(input(f"Player {turn}, enter position: ")))

    if position < 1 or position > 9:
     print("Invalid position! Choose a number between 1 and 9.")
     continue
    if board[position - 1] == "X" or board[position - 1] == "O":
     print("Position already taken!")
     continue

    board[position - 1] = turn
    if turn == "X":
        turn ="O"
    else:
        turn ="X"
    
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])
