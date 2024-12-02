import pygame
import sys
from chess import Board, Piece

pygame.init()

WIDTH, HEIGHT = 480, 480
SQUARE_SIZE = WIDTH // 8


# Load images
board_image = pygame.image.load("resources/board.png")

# Scale piece images to fit on squares
#for key in piece_images:
#    piece_images[key] = pygame.transform.scale(piece_images[key], (SQUARE_SIZE, SQUARE_SIZE))


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

def draw_board_and_pieces():
    # Draw the board
    screen.blit(board_image, (0, 0))

    # Draw the pieces
    for row in range(8):
        for col in range(8):
            piece = board.bstruct[row][col]
            if piece != " ":  # If there's a piece at this position
                x = col * SQUARE_SIZE
                y = row * SQUARE_SIZE
                screen.blit(piece.piece_img, (x, y))


board = Board()
running = True
# Game loop

x_in = None
x_out = None
y_in = None
y_out = None

while running:
    draw_board_and_pieces()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()
            col = mouse_x // SQUARE_SIZE
            row = mouse_y // SQUARE_SIZE

            if x_in is None and y_in is None:  
                x_in = row
                y_in = col

            elif x_out is None and y_out is None:

                x_out = row
                y_out = col
                action = board.process(x_in, y_in, x_out, y_out)
                x_in = None
                x_out = None
                y_in = None
                y_out = None
                
        pygame.display.flip()



