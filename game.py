import pygame
import sys
from chess import Board, Piece

pygame.init()

WIDTH, HEIGHT = 480, 480
SQUARE_SIZE = WIDTH // 8


board_image = pygame.image.load("resources/board.png")


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

def draw_board_and_pieces():
    screen.blit(board_image, (0, 0))

    for row in range(8):
        for col in range(8):
            piece = board.bstruct[row][col]
            if piece != " ":  
                x = col * SQUARE_SIZE
                y = row * SQUARE_SIZE
                screen.blit(piece.piece_img, (x, y))

def display_end_screen(text):
    screen.fill((0, 0, 0)) 
    font = pygame.font.Font(None, 50)
    text = font.render(text, True, (255, 255, 255)) 
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()



board = Board()
running = True
end = True


x_in = None
x_out = None
y_in = None
y_out = None

while running:
    draw_board_and_pieces()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            end = False
            break

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            col = mouse_x // SQUARE_SIZE
            row = mouse_y // SQUARE_SIZE

            if x_in is None and y_in is None:  
                x_in = row
                y_in = col
                highlight_color = (255, 255, 0, 128)  # Yellow translucent color
                highlight_surface = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
                highlight_surface.fill(highlight_color)
                screen.blit(highlight_surface, (col*SQUARE_SIZE, row*SQUARE_SIZE))

            elif x_out is None and y_out is None:

                x_out = row
                y_out = col
                running = board.process(x_in, y_in, x_out, y_out)
                x_in = None
                x_out = None
                y_in = None
                y_out = None
                
        pygame.display.flip()

while end:
    display_end_screen(board.message)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            end = False
            break
