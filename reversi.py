#Sohan Pujar, 30567556
import copy
def new_board():
    lst = [[0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,2,1,0,0,0],
           [0,0,0,1,2,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0]]
    return lst

def print_board(board):
    for i in range(0,8):
        row="" #initialises string
        for j in range(0,8): #scans whole list
            if board[i][j] == 1: 
                row += " B |" 
            elif board[i][j] == 2:
                row +=" W |"
            elif board[i][j] == 0:
                row += " - |"
        print(i+1,"|", row) #print the row
        
    print("     a   b   c   d   e   f   g   h")
    
def score(board):
    s1 = 0
    s2 = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                s1 += 1 
            elif board[i][j] == 2:
                s2 += 1 #adding to total
    return s1, s2

def enclosing(board, player, pos, Dir):
    if (pos[0] + Dir[0]) >= 0 and (pos[1] + Dir[1]) >= 0 and (pos[0] + Dir[0]) <= 7 and (pos[1] + Dir[1]) <= 7: #Incase it is on edges and goes so when add index the value can't go over 7 or below 1 out of bounds
        if not board[pos[0] + Dir[0]][pos[1]+ Dir[1]] == player and not board[pos[0] + Dir[0]][pos[1]+ Dir[1]] == 0: #To show tiles must be not our tiles
            for i in range(1,8):
                new_pos = [Dir[0]*i + pos[0], Dir[1]*i + pos[1]] #Define new_pos is after applying the direction
                if new_pos[0] >= 0 and new_pos[1]>= 0 and new_pos[0] <= 7 and new_pos[1] <= 7: #After applying direction the new_pos should be within range 
                    if board[new_pos[0]][new_pos[1]] == player: #If there is our tile after scanning the opposition tiles
                        return True
                    if board[new_pos[0]][new_pos[1]] == 0: #If there isn't our tile at the end after scanning the opposition tiles  
                        return False
    return False # Incase it goes out of range and if we add the direction to position an get player (us) or 0

#print(enclosing(new_board(), 1, (5,4), (-1,0)))

def valid_moves(board, player):
    moves = []
    Dir = [(0,-1),(0,1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1), (-1,1)] #All possible directions
    for i in range(0,8):
        for j in range(0,8):
            for k in range(len(Dir)):
                pos = (i,j) # for loops go through all possible indexes
                if enclosing(board, player, pos, Dir[k]) == True and board[pos[0]][pos[1]]==0: #if we are able to enclose in every possible direction which is the "for k loop" iteration
                    moves.append(pos) # Append our position to empty list of moves
                    break # So we don't append to our list multiple times
    return moves

def next_state(board, player, pos):
    Dir = [(0,-1),(0,1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1), (-1,1)]
    for i in Dir: 
        check = enclosing(board, player, pos, i) 
        if check == True: #Means 
            for j in range(1,8): 
                new_pos = [i[0]*j + pos[0], i[1]*j + pos[1]]
                if board[new_pos[0]][new_pos[1]] != player: #Can't be 0 as enclose checks and returns False
                    board[new_pos[0]][new_pos[1]] = player #flipping the opposition
                else:
                    break #End tile which is ours
    board[pos[0]][pos[1]] = player #start tile which is ours
    if player == 1:
        player = 2
    elif player == 2:
        player = 1 #Switching of players
    if valid_moves(board, player) == [] and player == 1:
        player = 2 
    if valid_moves(board, player) == [] and player == 2:
        player = 1 #Skipping turns
    if valid_moves(board, 1) == [] and valid_moves(board, 2) == []:
        player = 0 #game over
    return board, player

#print(next_state(new_board(), 1, (5,4)))

def pos(string):
    if string == "a1":
        return (0,0)
    elif string == "a2":
        return (1,0)
    elif string == "a3":
        return (2,0)
    elif string == "a4":
        return (3,0)
    elif string == "a5":
        return (4,0)
    elif string == "a6":
        return (5,0)
    elif string == "a7":
        return (6,0)
    elif string == "a8":
        return (7,0)
    elif string == "b1":
        return (0,1)
    elif string == "b2":
        return (1,1)
    elif string == "b3":
        return (2,1)
    elif string == "b4":
        return (3,1)
    elif string == "b5":
        return (4,1)
    elif string == "b6":
        return (5,1)
    elif string == "b7":
        return (6,1)
    elif string == "b8":
        return (7,1)
    elif string == "c1":
        return (0,2)
    elif string == "c2":
        return (1,2)
    elif string == "c3":
        return (2,2)
    elif string == "c4":
        return (3,2)
    elif string == "c5":
        return (4,2)
    elif string == "c6":
        return (5,2)
    elif string == "c7":
        return (6,2)
    elif string == "c8":
        return (7,2)
    elif string == "d1":
        return (0,3)
    elif string == "d2":
        return (1,3)
    elif string == "d3":
        return (2,3)
    elif string == "d4":
        return (3,3)
    elif string == "d5":
        return (4,3)
    elif string == "d6":
        return (5,3)
    elif string == "d7":
        return (6,3)
    elif string == "d8":
        return (7,3)
    elif string == "e1":
        return (0,4)
    elif string == "e2":
        return (1,4)
    elif string == "e3":
        return (2,4)
    elif string == "e4":
        return (3,4)
    elif string == "e5":
        return (4,4)
    elif string == "e6":
        return (5,4)
    elif string == "e7":
        return (6,4)
    elif string == "e8":
        return (7,4)
    elif string == "f1":
        return (0,5)
    elif string == "f2":
        return (1,5)
    elif string == "f3":
        return (2,5)
    elif string == "f4":
        return (3,5)
    elif string == "f5":
        return (4,5)
    elif string == "f6":
        return (5,5)
    elif string == "f7":
        return (6,5)
    elif string == "f8":
        return (7,5)
    elif string == "g1":
        return (0,6)
    elif string =="g2":
        return (1,6)
    elif string == "g3":
        return (2,6)
    elif string == "g4":
        return (3,6)
    elif string == "g5":
        return (4,6)
    elif string == "g6":
        return (5,6)
    elif string == "g7":
        return (6,6)
    elif string == "g8":
        return (7,6)
    elif string == "h1":
        return (0,7)
    elif string == "h2":
        return (1,7)
    elif string == "h3":
        return (2,7)
    elif string == "h4":
        return (3,7)
    elif string == "h5":
        return (4,7)
    elif string == "h6":
        return (5,7)
    elif string == "h7":
        return (6,7)
    elif string == "h8":
        return (7,7)
    else:
        return None #Associating human readable format of grid to indexes

def run_two_players():
    player = 1 #assumption to start off with black
    board = new_board() #starting off with new board
    while True:
        print_board(board)
        use = input("player {} Choose a valid move: ".format(player))#Strings are immutable
        if use == "q":
            return None #quit program
        pos_var = pos(use) #human input -> indexing on graph
        if pos_var is None:
            print("invalid move :(")
        else:
            if pos_var in valid_moves(board, player):
                board, player=next_state(board, player, pos_var)[0], next_state(board, player, pos_var)[1] #Does transition and flip
            else:
                print("invalid move :(")    #Not in valid moves
        if player == 0:
            if score(board)[0] > score(board)[1]: #Iterating through board
                print("Black won :)")
                return None
            elif score(board)[0] < score(board)[1]:
                print("White won :)")
                return None
            elif score(board)[0] == score(board)[1]:
                print("It's a DRAW!")
                return None

def max_index(valid_moves,board): 
    high_score = 0
    k = 0
    for i in range(len(valid_moves)):
        new_board = copy.deepcopy(board) #gets copy of board but doesn't change our current state of the board
        current_score = score(next_state(new_board,2,valid_moves[i])[0])[1] #current_score if we played that move
        if current_score > high_score:
            high_score = current_score #update score
            k = i #update index
    return k
            
    
def computer(board): #Decomposition
    k = max_index(valid_moves(board,2),board) #using max_index 
    return valid_moves(board,2)[k] #Computer is player 2 and returns the move with index k

def run_single_player():
    player = 1
    board = new_board()
    while True:
        print_board(board)
        if player == 1:
            use = input("player {} Choose a valid move: ".format(player))
        if player == 2:
            pos_var = computer(board) #computer doing move inputting coordinates
        if use == "q":
            return None
        if player == 1:
            pos_var = pos(use) #Changes to actual co-ordinate
        if pos_var is None:
            print("invalid move :(")
        else:
            if pos_var in valid_moves(board, player): #changing board and player if move is valid
                board, player = next_state(board, player, pos_var)[0], next_state(board, player, pos_var)[1]
            else:
                print("invalid move :(")
        if player == 0: #ending the game
            if score(board)[0] > score(board)[1]:
                print("Black won :)")
                return None
            elif score(board)[0] < score(board)[1]:
                print("White won :)")
                return None
            elif score(board)[0] == score(board)[1]:
                print("It's a DRAW!")
                return None

            
        




