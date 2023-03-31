# BattleShipGame
from random import randint

hidden_pattern = [[' ']*8 for x in range(8)]
guess_pattern = [[' ']*8 for x in range(8)]

let_to_num = {'A':0, "B":1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}

def print_board(board):
    print("  A B C D E F G H")
    print("   *************")
    row_num = 1
    for row in board:
        print(row_num, "|".join(row))
        row_num += 1

def get_ship_location(player):
    if player == "human":
        row = input("Please enter a ship row 1-8: ").upper()
        while row not in "12345678":
            print("Please enter a valid row")
            row = input("Please enter a ship row 1-8: ")
        column = input("Please enter a ship column A-H: ").upper()
        while column not in "ABCDEFGH":
            print("Please enter a valid column")
            column = input("Please enter a ship column A-H: ")
        return int(row)-1, let_to_num[column]
    elif player == "computer":
        row = randint(0, 7)
        column = randint(0, 7)
        return row, column

#Function that creates a ship
def create_ship(board, ship_size):
    while True:
        horizontal = randint(0, 1)
        if horizontal:
            row, col_start = randint(0,7), randint(0, 8 - ship_size)
            if any(board[row][col] == "X" for col in range(col_start, col_start + ship_size)):
                continue
            for col in range(col_start, col_start + ship_size):
                board[row][col] = "X"
            break
        else:
            col, row_start = randint(0, 7), randint(0,8 - ship_size)
            if any(board[row][col] == "X" for row in range(row_start, row_start + ship_size)):
                continue
            for row in range(row_start, row_start + ship_size):
                board[row][col] = "X"
            break

def create_all_ships(board):
    # The sizes of the 5 ships
    ship_sizes = [5, 4, 3, 3, 2]
    for ship_size in ship_sizes:
        create_ship(board, ship_size)


def count_hits(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

human_score = 0
computer_score = 0
create_all_ships(hidden_pattern)
print_board(hidden_pattern)
h_turns = 20
c_turns = 20
while h_turns > 0:
    print("Welcome to BattleShip Game")
    print_board(guess_pattern)
    row, column = get_ship_location("human")
    if guess_pattern[row][column] == "-":
        print("You have already guessed that ")
    elif hidden_pattern[row][column] == "X":
        print("You got em!")
        guess_pattern[row][column] = "X"
        human_score += 1
        h_turns -= 1
    else:
        print("Sorry, you missed :( ")
        guess_pattern[row][column] = "-"
        h_turns -= 1
    if count_hits(guess_pattern) == 14:
        print("Congratulations you have sunk all the battleships!!")
        break
    print("You have "+str(h_turns)+" turns remaining \n")

    # Computer player's turn
    print("Computer's turn:")
    row, column = get_ship_location("computer")
    if guess_pattern[row][column] == "-":
        print("The computer has already guessed that ")
    elif hidden_pattern[row][column] == "X":
        print("The computer got one!")
        guess_pattern[row][column] = "X"
        computer_score += 1
        c_turns -= 1
    else:
        print("The computer missed :( ")
        guess_pattern[row][column] = "-"
        c_turns -= 1
    if count_hits(guess_pattern) == 14:
        print("Congratulations you have sunk all the battleships!!")
        break
    print("You have "+str(c_turns)+" turns remaining \n")

    if h_turns == 0 and c_turns == 0:
        if human_score > computer_score:
            print("Congratulations! You won with a score:", human_score, "\n","Computer was not as good as you with a score:", computer_score)
        elif computer_score > human_score:
            print("This time computer was better with a score:", computer_score, "\n", "You got:", human_score)
        else:
            print("It is a tie! Score:", human_score)
        print("Game Over")
        break
