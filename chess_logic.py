
def findPieceIndex(piece_list, coords):
    """Finds the index of a piece at given coordinates."""
    for index, (piece_name, piece_coords) in enumerate(piece_list):
        if piece_coords == coords:
            return index
    return -1

def getValidMoves(index, whitePieces, blackPieces):
    pieceName = whitePieces[index][0]
    piecePos = whitePieces[index][1]
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
    if findPieceIndex(whitePieces + blackPieces, [piecePos[0], piecePos[1] - 1]) == -1:
        validMoves.append([piecePos[0], piecePos[1] - 1])
        if findPieceIndex(whitePieces + blackPieces, [piecePos[0], piecePos[1] - 2]) == -1:
            validMoves.append([piecePos[0], piecePos[1] - 2])
    if findPieceIndex(blackPieces, [piecePos[0] - 1, piecePos[1] - 1]) != -1:
        validMoves.append([piecePos[0] - 1, piecePos[1] - 1])
    if findPieceIndex(blackPieces, [piecePos[0] + 1, piecePos[1] - 1]) != -1:
        validMoves.append([piecePos[0] + 1, piecePos[1] - 1])
    return validMoves

def knight_valid_moves(piecePos, whitePieces, blackPieces):
    return 0

def bishop_valid_moves(piecePos, whitePieces, blackPieces):
    return 0

def rook_valid_moves(piecePos, whitePieces, blackPieces):
    return 0

def queen_valid_moves(piecePos, whitePieces, blackPieces):
    return 0

def king_valid_moves(piecePos, whitePieces, blackPieces):
    return 0