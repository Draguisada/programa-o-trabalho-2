# Criar Board N*N
# >=1 = Snake
# -1 = Maça



import random

def criarBoard(n):
    board = []
    height = int(n/2)
    for v in range(height):
        board.append([])
        for h in range(n):
            board[v].append(0)
    return board

def printBoard(board, n):
    out = ''
    print('-'*(n+2))
    for linha in board:
        out += '\n'
        out += '|'
        for caracter in linha:
            if caracter == 0:
                out += ' '
            elif caracter >= 1:
                out += '█'
            else:
                out += '◆'
        out += '|'
    print(out)
    print('-'*(n+2))

def updateBoard(board, sizeSnake):
    v = -1
    h = -1
    total = 0
    for linha in board:
        if total > sizeSnake:
            return
        v += 1
        h = -1
        for item in linha:
            if total > sizeSnake:
                return
            h += 1
            if item > 0:
                if item > sizeSnake:
                    board[v][h] = 0
                    continue
                board[v][h] += 1
                item =+ 1
                total += 1
                if item > sizeSnake:
                    board[v][h] = 0
            


def createFood(x, sizeHalf):
    i = 0
    while i < x :
        rand1 = random.randrange(0, sizeHalf)
        rand2 = random.randrange(0, sizeHalf)
        if board[rand1][rand2] == 0:
            board[rand1][rand2] = -1
            i += 1
    return x

def moveSnake(input=None, snakePos=[1, 0], board=None, size: int = 0, snakeSize = 1, foodInMap: int = 0):
    if input == 'w':
        if snakePos[0] - 1 >= 0:
            if board[snakePos[0]-1][snakePos[1]] == -1:
                snakeSize += 1
                foodInMap += 1
            snakePos[0] -= 1
    elif input == 'd':
        if snakePos[1] + 1 < size:
            if board[snakePos[0]][snakePos[1]+1] == -1:
                snakeSize += 1
                foodInMap += 1
            snakePos[1] += 1
    elif input == 's':
        if snakePos[0] + 1 < size:
            if board[snakePos[0]+1][snakePos[1]] == -1:
                snakeSize += 1
                foodInMap += 1
            snakePos[0] += 1
    elif input == 'a':
        if snakePos[1] - 1 >= 0:
            if board[snakePos[0]][snakePos[1]-1] == -1:
                snakeSize += 1
                foodInMap += 1
            snakePos[1] -= 1
    
    board[snakePos[0]][snakePos[1]] = 1
    return snakeSize, foodInMap
    


LastInput = 'd'

size = 20
sizeHalf = int(size/4)

snakePos = [sizeHalf, sizeHalf]

board = criarBoard(size)

food = 0
lastInput = 'd'
sizeSnake = 1
foodInMap = 0

board[snakePos[0]][snakePos[1]] = 1

while True:
    if foodInMap == 0:
        food += 1
    foodInMap = createFood(food, sizeHalf)
    food = 0

    printBoard(board, size)
    Input = input("Direção mover").lower()
    if Input == '':
        Input = lastInput
    updateBoard(board, sizeSnake)
    sizeSnake, foodInMapAtualizar = moveSnake(Input, snakePos, board, size, sizeSnake, foodInMap)
    foodInMap ^= foodInMapAtualizar
    
    lastInput = Input


