
board = [' ' for x in range(10)]

def insltr(letter, pos):
    board[pos] = letter

def spacefree(pos):
    return board[pos] == ' '

def prtbrd(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    
def winner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)

def usermove1():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spacefree(move):
                    run = False
                    insltr('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')
            
def usermove2():
    run = True
    while run:
        move = input('Please select a position to place an \'O\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spacefree(move):
                    run = False
                    insltr('O', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')

def compmove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if winner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
            
    if len(cornersOpen) > 0:
        move = selrandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
            
    if len(edgesOpen) > 0:
        move = selrandom(edgesOpen)
        
    return move

def selrandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
    

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    print("1.Single Player:")
    print("2.Double Player:")
    inp=input(str("Enter your choice:"))
    if inp=='1':
        
     print('Welcome to Tic Tac Toe!')
     prtbrd(board)


     while not(isBoardFull(board)):
         if not(winner(board, 'O')):
             usermove1()
             prtbrd(board)
         else:
             print('Sorry, O\'s won this time!')
             break
 
         if not(winner(board, 'X')):
             move = compmove()
             if move == 0:
                 print('Tie Game!')
             else:
                 insltr('O', move)
                 
                 print('Computer placed an \'O\' in position', move , ':')
                 prtbrd(board)
         else:
             print('X\'s won this time! Good Job!')
             break

   
    elif inp=='2':
        
      print('Welcome to Tic Tac Toe!')
      prtbrd(board)

      while not(isBoardFull(board)):
          if not(winner(board, 'O')):
              usermove1()
              prtbrd(board)
          else:
              print('O\'s won this time!')
              break
 
          if not(winner(board, 'X')):
              usermove2()
              prtbrd(board)
        
          else:
              print('X\'s won this time!')
              break



while True:
    answer = input('Do you want to play Tic-Tac-Toe? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break
