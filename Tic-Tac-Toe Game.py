#function to decide the markers for each player
def player_input():
    print(f"It is {player1_name}'s turn!")
    player1_marker = input("Please pick a marker 'X' or 'O':")
    while (player1_marker.upper() != "X"):
        while (player1_marker.upper() != "O"):
            if player1_marker.upper() == "X":
                break
            else:
                player1_marker = input("Please pick a marker 'X' or 'O':")
        break
    return player1_marker.upper()

#function to setup the board
from IPython.display import clear_output
def display_board(board):
    clear_output()
    #line 1
    print(f'      |     |     ')
    #line 2
    print(f'   {board[1]}  |  {board[2]}  |  {board[3]}')
    #line 3
    print(f'      |     |     ')
    #line 4
    print(f' -----------------')
    #line 5
    print(f'      |     |     ')
    #line 6
    print(f'   {board[4]}  |  {board[5]}  |  {board[6]}')
    #line 7
    print(f'      |     |     ')
    #line 8
    print(f' -----------------')
    #line 9
    print(f'      |     |     ')
    #line 10
    print(f'   {board[7]}  |  {board[8]}  |  {board[9]}')
    #line 11
    print(f'      |     |     ')
    print('Please press the number corresponding to the position for placing your marker.')

#function to check if board is full
def full_board_check(board):
    for i in range(1,10):
        if board[i] == i:
            return False
    return True

#function to let player choose the position
def player_choice(board):
    space = True
    while space:
        inputkey = input("Where do you want to place your marker?")
        if inputkey == "":
            position = 0
            print('Please enter a number between 1 and 9.')
        else:
            position = int(inputkey)
        while position > 9 or position < 1:
            position = int(input("Where do you want to place your marker?"))
        if board[position] == position:
            space = False
            return position
        else:
            print('That place is already taken! Try again')
    
#function to check for win
def win_check(board, mark):
    condition1 = test_board[1] == test_board[2] == test_board[3] == mark
    condition2 = test_board[1] == test_board[4] == test_board[7] == mark
    condition3 = test_board[1] == test_board[5] == test_board[9] == mark
    condition4 = test_board[7] == test_board[8] == test_board[9] == mark
    condition5 = test_board[3] == test_board[6] == test_board[9] == mark
    condition6 = test_board[3] == test_board[5] == test_board[7] == mark
    if condition1 == True or condition2 == True or condition3 == True or condition4 == True or condition5 == True or condition6 == True:
        return True
    else:
        return False

#function to replay the game
def replay():
    replay = input("Do you want to play again? Enter 'Y' or 'N':")
    while (replay.upper() != "Y"):
        while (replay.upper() != "N"):
            if replay.upper() == "Y":
                break
            else:
                replay = input("Do you want to play again? Enter 'Y' or 'N':")
        break
    if replay.upper() == "Y":
        return True
    else:
        return False
    
#Main game code:

while True:
    
    clear_output()
    print('Welcome to Tic Tac Toe!')

    #Enter player details
    import random
    player1_name = input("Please enter first player's name:")
    player2_name = input("Please enter second player's name:")
    first_player = random.randint(1,2)
    if first_player == 2:
        temp = player1_name
        player1_name = player2_name
        player2_name = temp
    print(f'{player1_name} plays first!')  
    
    #define the markers for both players
    if player_input() == "X":
        player1_marker = "X"
        player2_marker = "O"
    else:
        player2_marker = "X"
        player1_marker = "O"
    
    #printing the markers for both players
    print(f'{player1_name} will use marker {player1_marker}')
    print(f'{player2_name} will use marker {player2_marker}')

    #game board setup
    test_board = ['#',1,2,3,4,5,6,7,8,9]
    display_board(test_board)

    #main game play with two players taking turns
    which_player_turn = 1
    winner = ""
    while not full_board_check(test_board):
        if which_player_turn == 1:
            display_board(test_board)
            print(f"It is {player1_name}'s turn!")
            marker_position = player_choice(test_board)
            test_board[marker_position] = player1_marker
            which_player_turn = 2
            if win_check(test_board,player1_marker):
                display_board(test_board)
                winner = player1_name
                print(f'Congratulations! {player1_name} wins the game!')
                break
        else:
            display_board(test_board)
            print(f"It is {player2_name}'s turn!")
            marker_position = player_choice(test_board)
            test_board[marker_position] = player2_marker
            which_player_turn = 1
            if win_check(test_board,player2_marker):
                display_board(test_board)
                winner = player2_name
                print(f'Congratulations! {player2_name} wins the game!')
                break
    
    #message when the game is a draw
    if winner == "":
        display_board(test_board)
        print("Its a draw!")
    
    #check if the players want to play again
    if not replay():
        clear_output()
        print("Thank you for playing the game!")
        break