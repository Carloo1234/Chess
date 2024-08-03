canCastleLeft = True
canCastleRight = True


def findPieceIndex(piece_list, coords):
    """Finds the index of a piece at given coordinates."""
    for index, (piece_name, piece_coords) in enumerate(piece_list):
        if piece_coords == coords:
            return index
    return -1


def filterOutsideBoard(possibleMoves):
    validMoves = []
    for move in possibleMoves:
        if not (move[0] < 1 or move[0] > 8 or move[1] < 1 or move[1] > 8):
            validMoves.append(move)
    return validMoves


def filterOwnPieces(possibleMoves, whitePieces):
    validMoves = []
    for move in possibleMoves:
        if findPieceIndex(whitePieces, move) == -1:
            validMoves.append(move)
    return validMoves


def getValidMoves(pieceIndex, whitePieces, blackPieces):
    pieceName = whitePieces[pieceIndex][0]
    piecePos = whitePieces[pieceIndex][1]
    if pieceName == "Pawn":
        return pawn_valid_moves(piecePos, whitePieces, blackPieces)
    elif pieceName == "Rook":
        return rook_valid_moves(piecePos, whitePieces, blackPieces)
    elif pieceName == "Knight":
        return knight_valid_moves(piecePos, whitePieces, blackPieces)
    elif pieceName == "Bishop":
        return bishop_valid_moves(piecePos, whitePieces, blackPieces)
    elif pieceName == "Queen":
        return queen_valid_moves(piecePos, whitePieces, blackPieces)
    elif pieceName == "King":
        return king_valid_moves(piecePos, whitePieces, blackPieces)
    return []


def pawn_valid_moves(piecePos, whitePieces, blackPieces):
    validMoves = []
    possibleMoves = []
    if findPieceIndex(whitePieces + blackPieces, [piecePos[0], piecePos[1] - 1]) == -1:
        possibleMoves.append([piecePos[0], piecePos[1] - 1])
        if findPieceIndex(whitePieces + blackPieces, [piecePos[0], piecePos[1] - 2]) == -1 and piecePos[1] == 7:
            possibleMoves.append([piecePos[0], piecePos[1] - 2])
    if findPieceIndex(blackPieces, [piecePos[0] - 1, piecePos[1] - 1]) != -1:
        possibleMoves.append([piecePos[0] - 1, piecePos[1] - 1])
    if findPieceIndex(blackPieces, [piecePos[0] + 1, piecePos[1] - 1]) != -1:
        possibleMoves.append([piecePos[0] + 1, piecePos[1] - 1])
    filteredOutsideBoardMoves = filterOutsideBoard(possibleMoves)
    validMoves = filterOwnPieces(filteredOutsideBoardMoves, whitePieces)
    return validMoves


def knight_valid_moves(piecePos, whitePieces, blackPieces):
    possibleMoves = [
        [piecePos[0] + 1, piecePos[1] - 2],
        [piecePos[0] + 2, piecePos[1] - 1],
        [piecePos[0] + 2, piecePos[1] + 1],
        [piecePos[0] + 1, piecePos[1] + 2],
        [piecePos[0] - 1, piecePos[1] + 2],
        [piecePos[0] - 2, piecePos[1] + 1],
        [piecePos[0] - 2, piecePos[1] - 1],
        [piecePos[0] - 1, piecePos[1] - 2],
    ]
    filteredOutsideBoardMoves = filterOutsideBoard(possibleMoves)
    validMoves = filterOwnPieces(filteredOutsideBoardMoves, whitePieces)
    return validMoves


def bishop_valid_moves(piecePos, whitePieces, blackPieces):
    possibleMoves = []
    # Top right
    for i in range(1, 9):
        move = [piecePos[0] + i, piecePos[1] - i]
        possibleMoves.append(move)
        if findPieceIndex(blackPieces + whitePieces, move) != -1:
            break
    # Top left
    for i in range(1, 9):
        move = [piecePos[0] - i, piecePos[1] - i]
        possibleMoves.append(move)
        if findPieceIndex(blackPieces + whitePieces, move) != -1:
            break
    # Bottom right
    for i in range(1, 9):
        move = [piecePos[0] + i, piecePos[1] + i]
        possibleMoves.append(move)
        if findPieceIndex(blackPieces + whitePieces, move) != -1:
            break
    # Bottom left
    for i in range(1, 9):
        move = [piecePos[0] - i, piecePos[1] + i]
        possibleMoves.append(move)
        if findPieceIndex(blackPieces + whitePieces, move) != -1:
            break
    filteredOutsideBoardMoves = filterOutsideBoard(possibleMoves)
    validMoves = filterOwnPieces(filteredOutsideBoardMoves, whitePieces)
    return validMoves


def rook_valid_moves(piecePos, whitePieces, blackPieces):
    possibleMoves = []
    # Up
    for i in range(1, 9):
        move = [piecePos[0], piecePos[1] - i]
        possibleMoves.append(move)
        if findPieceIndex(blackPieces + whitePieces, move) != -1:
            break
    # Down
    for i in range(1, 9):
        move = [piecePos[0], piecePos[1] + i]
        possibleMoves.append(move)
        if findPieceIndex(blackPieces + whitePieces, move) != -1:
            break
    # Right
    for i in range(1, 9):
        move = [piecePos[0] + i, piecePos[1]]
        possibleMoves.append(move)
        if findPieceIndex(blackPieces + whitePieces, move) != -1:
            break
    # Left
    for i in range(1, 9):
        move = [piecePos[0] - i, piecePos[1]]
        possibleMoves.append(move)
        if findPieceIndex(blackPieces + whitePieces, move) != -1:
            break
    filteredOutsideBoardMoves = filterOutsideBoard(possibleMoves)
    validMoves = filterOwnPieces(filteredOutsideBoardMoves, whitePieces)
    return validMoves


def queen_valid_moves(piecePos, whitePieces, blackPieces):
    possibleMoves = []
    # Top right
    for i in range(1, 9):
        move = [piecePos[0] + i, piecePos[1] - i]
        possibleMoves.append(move)
        if findPieceIndex(blackPieces + whitePieces, move) != -1:
            break
    # Top left
    for i in range(1, 9):
        move = [piecePos[0] - i, piecePos[1] - i]
        possibleMoves.append(move)
        if findPieceIndex(blackPieces + whitePieces, move) != -1:
            break
    # Bottom right
    for i in range(1, 9):
        move = [piecePos[0] + i, piecePos[1] + i]
        possibleMoves.append(move)
        if findPieceIndex(blackPieces + whitePieces, move) != -1:
            break
    # Bottom left
    for i in range(1, 9):
        move = [piecePos[0] - i, piecePos[1] + i]
        possibleMoves.append(move)
        if findPieceIndex(blackPieces + whitePieces, move) != -1:
            break
    # Up
    for i in range(1, 9):
        move = [piecePos[0], piecePos[1] - i]
        possibleMoves.append(move)
        if findPieceIndex(blackPieces + whitePieces, move) != -1:
            break
    # Down
    for i in range(1, 9):
        move = [piecePos[0], piecePos[1] + i]
        possibleMoves.append(move)
        if findPieceIndex(blackPieces + whitePieces, move) != -1:
            break
    # Right
    for i in range(1, 9):
        move = [piecePos[0] + i, piecePos[1]]
        possibleMoves.append(move)
        if findPieceIndex(blackPieces + whitePieces, move) != -1:
            break
    # Left
    for i in range(1, 9):
        move = [piecePos[0] - i, piecePos[1]]
        possibleMoves.append(move)
        if findPieceIndex(blackPieces + whitePieces, move) != -1:
            break
    filteredOutsideBoardMoves = filterOutsideBoard(possibleMoves)
    validMoves = filterOwnPieces(filteredOutsideBoardMoves, whitePieces)
    print(validMoves)
    return validMoves


def king_valid_moves(piecePos, whitePieces, blackPieces):
    possibleMoves = [
        [piecePos[0] + 1, piecePos[1]],
        [piecePos[0] - 1, piecePos[1]],
        [piecePos[0], piecePos[1] + 1],
        [piecePos[0], piecePos[1] - 1],
        [piecePos[0] + 1, piecePos[1] + 1],
        [piecePos[0] - 1, piecePos[1] - 1],
        [piecePos[0] + 1, piecePos[1] - 1],
        [piecePos[0] - 1, piecePos[1] + 1],
    ]
    if checkIfCanCastleLeft(whitePieces + blackPieces, piecePos):
        possibleMoves.append([piecePos[0] - 2, piecePos[1]])
    if checkIfCanCastleRight(whitePieces + blackPieces, piecePos):
        possibleMoves.append([piecePos[0] + 2, piecePos[1]])
    filteredOutsideBoardMoves = filterOutsideBoard(possibleMoves)
    validMoves = filterOwnPieces(filteredOutsideBoardMoves, whitePieces)
    return validMoves


def checkIfCanCastleLeft(allPieces, piecePos):
    if canCastleLeft:
        positionsToCheck = [[2, 8], [3, 8], [4, 8]]
        # check no pieces are between king and rook
        for position in positionsToCheck:
            if findPieceIndex(allPieces, position) != -1:
                return False
        return True


def checkIfCanCastleRight(allPieces, piecePos):
    if canCastleRight:
        print("test 1 passed")
        positionsToCheck = [[6, 8], [7, 8]]
        # check no pieces are between king and rook
        for position in positionsToCheck:
            if findPieceIndex(allPieces, position) != -1:
                return False
        return True
