import random
import time
import sys
import pprint

Author = "Ayotunde Okunubi"
Updated = "20/8/2020"

players = {}

board = {
    1:'', 2:'', 3:'',
    4:'', 5:'', 6:'',
    7:'', 8:'', 9:'',
}

winningSequence = [[1,4,7], [2,5,8], [3,6,9], [1,2,3], [4,5,6], [7,8,9], [1,5,9],
                   [3,5,7]]

def checkWin(board, winSeq, player):
    global players
    if type(winSeq) is not list:
        print("Winning sequnce must be a list")
        sys.exit()
    else:
        boardIndex = list(board.keys())
        #print(boardIndex)
        for i in range(0, len(winSeq)):
            subList = winSeq[i]
            x,y,z = subList
            if board[x] == players[player] and board[y] == players[player] and board[z] == players[player]:
                print("You WIn", player, '...')
                time.sleep(3)
                sys.exit()
                                                                                       
    
def printBoard(board):
    for i in range (1, len(board)+1):
        print (i,'|',board[i],'|', end = '      ',)
        if i%3 == 0:
            print(end='\n\n\n')
            

def takeInput(player, board):
    expMarker = ""
    if player == "Player1":
        expMarker = "X"
    else:
        expMarker = "O"
    entry = input("Please input your entry")

    while expMarker not in entry:
        entry = input("Incorrect marker, Pls enter your entry")
    
    if expMarker in entry:
        entryList = list(entry)
        
        while len(entryList) > 2 or len(entryList)<2:
            print ("Input Error, pls check your input")
            entry = input("Incorrect marker, Pls enter your entry")
            entryList = list(entry)  
                
        else:
            print (player, ' ', "entered" + ' '+ entry)
            board[int(entry[0])] = str(entry[1])
            printBoard(board)
    else:
        print (player, '', "That is not your Marker")
        sys.exit()


def main(board):
    printBoard(board)
    global players
    players = {'Player1':'X', 'Player2':'O'}
    playersList = list(players.keys())
    firstPlay = random.choice(playersList)
    playersList.remove(firstPlay)
    secondPlay = playersList[0]
    while '' in board.values():
        print (firstPlay + ' ,'+"It's your turn...")
        time.sleep(2)
        takeInput(firstPlay, board)
        checkWin(board, winningSequence, firstPlay)
        

        if '' in board.values():
            print (secondPlay+ ' ,' + "It's your turn...")
            time.sleep(2)
            takeInput(secondPlay, board)
            checkWin(board, winningSequence, secondPlay)
        else:
            continue
    else:
        print ("No more moves, Its a Tie")

main(board)


#----------------------
#Notes
"""
Improve commenting on program
update program to validate input thoroughly
"""
