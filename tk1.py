def my_sum(a, b, c):
    return a + b + c

def printBoard(xState, zState):
    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)
    print(f"{zero} | {one} | {two}")
    print("--|---|---")
    print(f"{three} | {four} | {five}")
    print("--|---|---")
    print(f"{six} | {seven} | {eight}")

def checkWin(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if my_sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            print("X won the match")
            return 1
        if my_sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            print("O won the match")
            return 0
    return -1

if __name__ == "__main__":
    xState = [0] * 9
    zState = [0] * 9    
    turn = 1  # 1 for X and 0 for O
    print("Welcome to Tic Tac Toe")
    while True:
        printBoard(xState, zState)
        if turn == 1:
            print("X's Chance")
        else:
            print("O's Chance")
        
        while True:
            try:
                value = int(input("Please enter a value (0-8): "))
                if value < 0 or value > 8:
                    print("Invalid input. Please enter a number between 0 and 8.")
                elif (turn == 1 and xState[value] != 0) or (turn == 0 and zState[value] != 0):
                    print("Cell already taken. Please choose another cell.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        if turn == 1:
            xState[value] = 1
        else:
            zState[value] = 1
        
        cwin = checkWin(xState, zState)
        if cwin != -1:
            printBoard(xState, zState)
            print("Match over")
            break
        
        turn = 1 - turn