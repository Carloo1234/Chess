import pygame

import chess_logic

pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

BOARD_WIDTH = 480
BOARD_HEIGHT = 480
TILE_SIZE = BOARD_WIDTH / 8

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((0, 0, 0))
pygame.display.set_caption("Poopy chess game")
clock = pygame.time.Clock()
boardSurface = pygame.Surface((BOARD_WIDTH, BOARD_HEIGHT))
boardSurface.fill("Red")
run = True
turn = "white"

whitePawn = pygame.image.load('assets/pieces/white_pawn.png')
whitePawn = pygame.transform.scale(whitePawn, (45, 45))

whiteRook = pygame.image.load('assets/pieces/white_rook.png')
whiteRook = pygame.transform.scale(whiteRook, (45, 45))

whiteKnight = pygame.image.load('assets/pieces/white_knight.png')
whiteKnight = pygame.transform.scale(whiteKnight, (45, 45))

whiteBishop = pygame.image.load('assets/pieces/white_bishop.png')
whiteBishop = pygame.transform.scale(whiteBishop, (45, 45))

whiteQueen = pygame.image.load('assets/pieces/white_queen.png')
whiteQueen = pygame.transform.scale(whiteQueen, (45, 45))

whiteKing = pygame.image.load('assets/pieces/white_king.png')
whiteKing = pygame.transform.scale(whiteKing, (45, 45))

# Load and scale black pieces
blackPawn = pygame.image.load('assets/pieces/black_pawn.png')
blackPawn = pygame.transform.scale(blackPawn, (45, 45))

blackRook = pygame.image.load('assets/pieces/black_rook.png')
blackRook = pygame.transform.scale(blackRook, (45, 45))

blackKnight = pygame.image.load('assets/pieces/black_knight.png')
blackKnight = pygame.transform.scale(blackKnight, (45, 45))

blackBishop = pygame.image.load('assets/pieces/black_bishop.png')
blackBishop = pygame.transform.scale(blackBishop, (45, 45))

blackQueen = pygame.image.load('assets/pieces/black_queen.png')
blackQueen = pygame.transform.scale(blackQueen, (45, 45))

blackKing = pygame.image.load('assets/pieces/black_king.png')
blackKing = pygame.transform.scale(blackKing, (45, 45))

gridPositions = {}
selectionStatus = [False, [0, 0]]
# White pieces starting positions
whitePieces = [
    ['Rook', [1, 8]],
    ['Knight', [2, 8]],
    ['Bishop', [3, 8]],
    ['Queen', [4, 8]],
    ['King', [5, 8]],
    ['Bishop', [6, 8]],
    ['Knight', [7, 8]],
    ['Rook', [8, 8]],
    ['Pawn', [1, 7]],
    ['Pawn', [2, 7]],
    ['Pawn', [3, 7]],
    ['Pawn', [4, 7]],
    ['Pawn', [5, 7]],
    ['Pawn', [6, 7]],
    ['Pawn', [7, 7]],
    ['Pawn', [8, 7]]
]

blackPieces = [
    ['Rook', [1, 1]],
    ['Knight', [2, 1]],
    ['Bishop', [3, 1]],
    ['Queen', [4, 1]],
    ['King', [5, 1]],
    ['Bishop', [6, 1]],
    ['Knight', [7, 1]],
    ['Rook', [8, 1]],
    ['Pawn', [1, 2]],
    ['Pawn', [2, 2]],
    ['Pawn', [3, 2]],
    ['Pawn', [4, 2]],
    ['Pawn', [5, 2]],
    ['Pawn', [6, 2]],
    ['Pawn', [7, 2]],
    ['Pawn', [8, 2]]
]

validMoves = []


def drawBoard():
    for column in range(8):
        for row in range(8):
            if (row + column) % 2:
                pygame.draw.rect(boardSurface, "gray", [60 * row, 60 * column, 60, 60])
                gridPositions.update({(column + 1, row + 1): (6 + (column * 60), 6 + (row * 60))})
            else:
                pygame.draw.rect(boardSurface, "white", [60 * row, 60 * column, 60, 60])
                gridPositions.update({(column + 1, row + 1): (6 + (column * 60), 6 + (row * 60))})


def drawPieces():
    for piece in whitePieces:
        pos = (piece[1][0], piece[1][1])
        if piece[0] == "Rook":
            boardSurface.blit(whiteRook, (gridPositions.get(pos)))
        elif piece[0] == "Bishop":
            boardSurface.blit(whiteBishop, (gridPositions.get(pos)))
        elif piece[0] == "Knight":
            boardSurface.blit(whiteKnight, (gridPositions.get(pos)))
        elif piece[0] == "Queen":
            boardSurface.blit(whiteQueen, (gridPositions.get(pos)))
        elif piece[0] == "King":
            boardSurface.blit(whiteKing, (gridPositions.get(pos)))
        elif piece[0] == "Pawn":
            boardSurface.blit(whitePawn, (gridPositions.get(pos)))
    for piece in blackPieces:
        pos = (piece[1][0], piece[1][1])
        if piece[0] == "Rook":
            boardSurface.blit(blackRook, (gridPositions.get(pos)))
        elif piece[0] == "Bishop":
            boardSurface.blit(blackBishop, (gridPositions.get(pos)))
        elif piece[0] == "Knight":
            boardSurface.blit(blackKnight, (gridPositions.get(pos)))
        elif piece[0] == "Queen":
            boardSurface.blit(blackQueen, (gridPositions.get(pos)))
        elif piece[0] == "King":
            boardSurface.blit(blackKing, (gridPositions.get(pos)))
        elif piece[0] == "Pawn":
            boardSurface.blit(blackPawn, (gridPositions.get(pos)))
    for move in validMoves:
        circlePos = (gridPositions.get(tuple(move)))
        pygame.draw.circle(boardSurface, "light green", (circlePos[0] + 24, circlePos[1] + 24), 10)

while run:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()

            # Check if the click is on the board
            if not (360 < mousePos[0] < 840 and mousePos[1] < 480):
                continue

            # Calculate board coordinates from mouse position
            xPos = ((mousePos[0] - 360) // 60) + 1
            yPos = (mousePos[1] // 60) + 1
            clickCoords = [xPos, yPos]

            # Check if the clicked square contains a white piece
            clickedPieceIndex = chess_logic.findPieceIndex(whitePieces, clickCoords)

            if clickedPieceIndex != -1:
                # Clicked on a square with a white piece
                selectionStatus[0] = True
                selectionStatus[1] = clickCoords
                validMoves = chess_logic.getValidMoves(clickedPieceIndex, whitePieces, blackPieces)
                continue

            # Clicked on an empty square or a square with a black piece
            if not selectionStatus[0]:
                continue

            # Handle movement to a valid square
            selectedPieceIndex = chess_logic.findPieceIndex(whitePieces, selectionStatus[1])
            if clickCoords in validMoves:
                # Check if you can castle(Rooks)
                if whitePieces[selectedPieceIndex][0] == 'Rook':
                    # Check left castle
                    if whitePieces[selectedPieceIndex][1] == [1, 8]:
                        chess_logic.canCastleLeft = False
                        print("Cannot castle left")
                    # Check right castle
                    elif whitePieces[selectedPieceIndex][1] == [8, 8]:
                        chess_logic.canCastleRight = False
                        print("Cannot castle right")
                # Check if you can castle(King)
                elif whitePieces[selectedPieceIndex][0] == "King":
                    chess_logic.canCastleRight = False
                    chess_logic.canCastleLeft = False

                # Move the selected piece to the new position
                whitePieces[selectedPieceIndex][1] = clickCoords

                # Check if a black piece is on the target square and remove it if present
                takePieceIndex = chess_logic.findPieceIndex(blackPieces, clickCoords)
                if takePieceIndex != -1:
                    blackPieces.remove(blackPieces[takePieceIndex])

            # Reset selection after move
            selectionStatus[0] = False
            validMoves = []

    screen.blit(boardSurface, (600 - (BOARD_WIDTH / 2), 0))
    drawBoard()
    drawPieces()
    clock.tick(60)
pygame.quit()
