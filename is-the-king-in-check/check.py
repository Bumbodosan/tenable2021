'''
Takes '+' and ' ' delimited data of chess matches and parses into list of seperate matches
'''
def ParseMatches(chess_matches):
    return [c.split('+') for c in chess_matches.split(' ')]


x_axis = "abcdefgh"

colors = ["b", "w"]
pieces = ["q", "k", "b", "r", "n", "p"]

board = [[(None, None) for x in range(8)] for y in range(8)]

def getCoord(coord):
    x = x_axis.index(coord[0])
    y = int(coord[1]) - 1
    return x, y

def checkPiece(board, piece, x, y):
    return board[y][x] == piece

def moveloop(board, x, y, dx, dy, piecesToCheck):
    currentcolor = board[y][x][0]
    tempx = x+dx
    tempy = y+dy
    while tempy + dy < 7 and tempy + dy > 0 and tempx + dx < 7 and tempx + dx > 0:
        tempx += dx
        tempy += dy
        pieceAtPos = board[tempy][tempx]
        if currentcolor == pieceAtPos[0]:
            continue
        if any(pieceAtPos[1] == pieces.index(piece) for piece in piecesToCheck):
            return True
    return False

def rook(board, x, y):
    for direction in range(0, 4):
        dx = 0 if direction % 2 == 0 else direction - 2
        dy = 0 if direction % 2 == 1 else direction - 1
        runsinto = moveloop(board, x, y, dx, dy, ["r", "q"])
        if runsinto == True:
            return True

    return False

def bishop(board, x, y):
    for ydir in range(0, 2):
        dy = -1 + (ydir * 2)
        for xdir in range(0, 2):
            dx = -1 + (xdir * 2)
            runsinto = moveloop(board, x, y, dx, dy, ["b", "q"])
            if runsinto == True:
                return True
    return False

def knight(board, x, y):
    currentcolor = board[y][x][0]
    for direction in range(0, 4):
        dx = 0 if direction % 2 == 0 else (direction - 2) * 2
        dy = 0 if direction % 2 == 1 else (direction - 1) * 2
        for deg in range(0, 2):
            if direction % 2 != 1:
                dx = -1 + (deg * 2)
            elif direction % 2 != 0:
                dy = -1 + (deg * 2)
            newy = y + dy
            newx = x + dx
            if newy > 7 or newy < 0 or newx > 7 or newx < 0:
                continue
            pieceAtPos = board[newy][newx]
            if currentcolor == pieceAtPos[0]:
                continue
            if pieceAtPos[1] == pieces.index("n"):
                return True
    return False

def pawn(board, x, y):
    currentcolor = board[y][x][0]
    dy = 1 if currentcolor == colors.index("w") else -1
    for xdir in range(0, 2):
        dx = -1 + (xdir * 2)
        newy = y + dy
        newx = x + dx
        if newy > 7 or newy < 0 or newx > 7 or newx < 0:
            continue
        pieceAtPos = board[newy][newx]
        if currentcolor == pieceAtPos[0]:
            continue
        if pieceAtPos[1] == pieces.index("p"):
            return True
    return False

def king(board, x, y):
    currentcolor = board[y][x][0]
    for direction in range(0, 4):
        dx = 0 if direction % 2 == 0 else (direction - 2)
        dy = 0 if direction % 2 == 1 else (direction - 1)
        for deg in range(0, 3):
            if direction % 2 != 1:
                dx = -1 + deg
            elif direction % 2 != 0:
                dy = -1 + deg
            newy = y + dy
            newx = x + dx
            if newy > 7 or newy < 0 or newx > 7 or newx < 0:
                continue
            pieceAtPos = board[newy][newx]
            if currentcolor == pieceAtPos[0]:
                continue
            if pieceAtPos[1] == pieces.index("k"):
                return True
    return False

def checkPieces(board, pos):
    return rook(board, pos[0], pos[1]) or bishop(board, pos[0], pos[1]) or knight(board, pos[0], pos[1]) or pawn(board, pos[0], pos[1]) or king(board, pos[0], pos[1])

def IsKingInCheck(chess_match):
    whiteking = None
    blackking = None
    for info in chess_match:
        split = info.split(",")
        color = colors.index(split.pop(0))
        piece = pieces.index(split.pop(0))
        x, y = getCoord(split.pop(0))
        board[y][x] = (color, piece)
        if piece == pieces.index("k"):
            if color == colors.index("w"):
                whiteking = (x, y)
            else:
                blackking = (x, y)

    return checkPieces(board, whiteking)

result = []
chess_matches = ParseMatches(raw_input())
for chess_match in chess_matches:
    result.append(IsKingInCheck(chess_match))

print result
