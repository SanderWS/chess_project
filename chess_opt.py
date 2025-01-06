import pygame
import pandas as pd
import numpy as np


class Piece:
    def __init__(self, position, p_type, color, img):
        self.type = p_type
        self.color = color
        self.position = position

        self.piece_id = 0
        self.en_passant = False
        self.piece_img = pygame.image.load(img)
        if self.type == "Pawn":
            self.first_move = True

    def __str__(self):
        return self.type

class Board:
    def __init__(self):
        self.bstruct = [[" " for i in range(8)] for j in range(8)]
        #self.bstruct = pd.DataFrame()
        self.set_up()
        self.color = "White"
        self.opp_color = "Black"
        self.SQUARE_SIZE = 60
        self.x_in = None
        self.x_out = None
        self.y_in = None
        self.y_out = None
        self.message = ""

    def __str__(self):
        return self.message

    def coordinate_conv(self, a):
        letters = "ABCDEFGH"
        letter_dict = {letter : (numb + 1)  for numb, letter in enumerate(letters)}
        number_dict = {(numb + 1) : letter  for numb, letter in enumerate(letters)}

        if isinstance(a, str) and (a.upper() in letters):
            a = a.upper()
            return number_dict[a]
        elif isinstance(a, int) and (a in range(8)):
            return letter_dict[a]
    
    def swap_color(self):
        if self.color == "White":
            self.opp_color = self.color
            self.color = "Black"
        else:
            self.opp_color = self.color
            self.color = "White"


    def set_up(self):

        for i in range(8):
            self.bstruct[1][i] = Piece("Pawn", "Black", "resources/b_pawn.png")
            self.bstruct[6][i] = Piece("Pawn", "White", "resources/w_pawn.png")

        # Black Pieces
        self.bstruct[0][0] = Piece("Rook", "Black", "resources/b_rook.png")
        self.bstruct[0][7] = Piece("Rook", "Black", "resources/b_rook.png")

        self.bstruct[0][1] = Piece("Knight", "Black", "resources/b_knight.png")
        self.bstruct[0][6] = Piece("Knight", "Black", "resources/b_knight.png")

        self.bstruct[0][2] = Piece("Bishop", "Black", "resources/b_bishop.png")
        self.bstruct[0][5] = Piece("Bishop", "Black", "resources/b_bishop.png")

        self.bstruct[0][4] = Piece("King", "Black", "resources/b_king.png")
        self.bstruct[0][3] = Piece("Queen", "Black", "resources/b_queen.png")

        # White Pieces
        self.bstruct[7][0] = Piece("Rook", "White", "resources/w_rook.png")
        self.bstruct[7][7] = Piece("Rook", "White", "resources/w_rook.png")

        self.bstruct[7][1] = Piece("Knight", "White", "resources/w_knight.png")
        self.bstruct[7][6] = Piece("Knight", "White", "resources/w_knight.png")

        self.bstruct[7][2] = Piece("Bishop", "White", "resources/w_bishop.png")
        self.bstruct[7][5] = Piece("Bishop", "White", "resources/w_bishop.png")

        self.bstruct[7][4] = Piece("King", "White", "resources/w_king.png")
        self.bstruct[7][3] = Piece("Queen", "White", "resources/w_queen.png")


    def process(self, x_in, y_in, x_out, y_out):
        
        self.x_in = x_in
        self.x_out = x_out
        self.y_in = y_in
        self.y_out = y_out

        if self.x_in == self.x_out and self.y_in == self.y_out:
            self.illegal()
            return True
        
        elif self.check_legal() and not self.output_in_check():
            self.move()

            if not self.has_moves() and self.in_check():
                self.message = f"{self.opp_color} wins!"
                return False
            
            elif not self.has_moves():
                self.message = "Draw!"
                return False
            
            return True
        return True
                
        

    def print_board(self):
        print()
        df = pd.DataFrame(self.bstruct)
        print(df)
        print()

    def illegal(self):
        pass
    
    def check_legal(self):

        obj = self.bstruct[self.x_in][self.y_in]

        if self.bstruct[self.x_in][self.y_in] == " ":
            self.illegal()
            return 

        elif obj.color != self.color :
            self.illegal()
            return 
        
        elif (isinstance(obj, Piece) and obj.type == "Pawn"):
            sign = 1
            if obj.color == "White":
                sign = -1
 
            if (self.bstruct[self.x_out][self.y_out] == " ") and (self.y_out - self.y_in == 0):
                if (self.x_out - self.x_in == sign*1):
                    obj.first_move = False
                    return True

                elif (self.x_out - self.x_in == sign*2) and obj.first_move:
                    if self.check_empty():

                        return True
                else:
                    self.illegal()
                    
            elif (self.x_out - self.x_in == sign*1) and (abs(self.y_out - self.y_in) == 1):
                if isinstance(self.bstruct[self.x_out][self.y_out], Piece) and self.bstruct[self.x_out][self.y_out].color != self.color:
                    return True
                elif (isinstance(self.bstruct[-1*sign + self.x_out][self.y_out], Piece)) and self.bstruct[-1*sign + self.x_out][self.y_out].en_passant:
                    self.bstruct[-1*sign + self.x_out][self.y_out] = " "
                    return True

            else:
                self.illegal()
                

        elif (isinstance(obj, Piece) and obj.type == "Rook"):
            if (self.x_in != self.x_out) and (self.y_in != self.y_out):
                self.illegal()
                return False
            
            elif self.check_empty():
                return True
            
            else:
                self.illegal()
                return False
            
            
        elif (isinstance(obj, Piece) and obj.type == "Knight"):
            if (abs(self.x_out - self.x_in) == 2) and (abs(self.y_out - self.y_in) == 1):
                if self.bstruct[self.x_out][self.y_out] == " ":
                    return True
            
                elif self.bstruct[self.x_out][self.y_out].color != self.color:
                    return True
                
                else:
                    self.illegal()
                    return False

            elif (abs(self.x_out - self.x_in) == 1) and (abs(self.y_out - self.y_in) == 2):
                if self.bstruct[self.x_out][self.y_out] == " ":
                    return True
            
                elif self.bstruct[self.x_out][self.y_out].color != self.color:
                    return True
                
                else:
                    self.illegal()
                    return False
            else:
                self.illegal()
                return False

            
        elif (isinstance(obj, Piece) and obj.type == "Bishop"):
            if (self.x_out - self.x_in != 0) and (self.y_out - self.y_in != 0):
                if (abs((self.x_out - self.x_in)/(self.y_out - self.y_in)) == 1) and self.check_empty():
                    return True
                    
                else:
                    self.illegal()
                    return False
            else:
                self.illegal()
                return False
            
        elif (isinstance(obj, Piece) and obj.type == "King"):
            if (abs(self.x_out - self.x_in) < 2) and (abs(self.y_out - self.y_in) < 2):
                if self.check_empty():
                    return True
                else:
                    self.illegal()
                    return False
            else:
                self.illegal()
                return False
                    
                
        elif (isinstance(obj, Piece) and obj.type == "Queen"):
            if (self.x_out - self.x_in != 0) and (self.y_out - self.y_in != 0):
                if (abs((self.x_out - self.x_in)/(self.y_out - self.y_in)) == 1) and self.check_empty():
                    return True
                    
                else:
                    self.illegal()
                    return False
                
            elif (self.x_in == self.x_out) or (self.y_in == self.y_out) and self.check_empty():
                return True
            
            else:
                self.illegal()
                return False
            
    def in_check(self):
        temp_x_in, temp_y_in, temp_x_out, temp_y_out = self.x_in, self.y_in, self.x_out, self.y_out
        self.swap_color()
        for i in range(8):
            for j in range(8):
                if isinstance(self.bstruct[i][j], Piece) and self.bstruct[i][j].type == "King":
                    if self.bstruct[i][j].color == self.opp_color:
                        self.x_out, self.y_out = i, j

                        break
        
        for i in range(8):
            for j in range(8):
                if isinstance(self.bstruct[i][j], Piece) and self.bstruct[i][j].color == self.color:
                    self.x_in, self.y_in = i, j
                    if self.check_legal():
                        self.x_in, self.y_in, self.x_out, self.y_out = temp_x_in, temp_y_in, temp_x_out, temp_y_out
                        self.swap_color()
                        return True
                    
        self.x_in, self.y_in, self.x_out, self.y_out = temp_x_in, temp_y_in, temp_x_out, temp_y_out
        self.swap_color()
        return False

    def output_in_check(self):
        temp_input = self.bstruct[self.x_in][self.y_in]
        temp_output = self.bstruct[self.x_out][self.y_out]

        self.bstruct[self.x_out][self.y_out] = self.bstruct[self.x_in][self.y_in]
        self.bstruct[self.x_in][self.y_in] = " "

        
        if self.in_check():
            self.bstruct[self.x_in][self.y_in] = temp_input
            self.bstruct[self.x_out][self.y_out] = temp_output
            
            return True


        self.bstruct[self.x_in][self.y_in] = temp_input
        self.bstruct[self.x_out][self.y_out] = temp_output

        return False
    
    
    def has_moves(self):

        temp_x_in, temp_y_in, temp_x_out, temp_y_out = self.x_in, self.y_in, self.x_out, self.y_out

        for x_input in range(8):
            for y_input in range(8):
                if isinstance(self.bstruct[x_input][y_input], Piece) and self.bstruct[x_input][y_input].color == self.color:
                    self.x_in, self.y_in = x_input, y_input
                    for x_output in range(8):
                        for y_output in range(8):
                            self.x_out, self.y_out = x_output, y_output 
                            if self.check_legal() and not self.output_in_check():
                                    self.x_in, self.y_in, self.x_out, self.y_out = temp_x_in, temp_y_in, temp_x_out, temp_y_out
                                    return True
                            
        self.x_in, self.y_in, self.x_out, self.y_out = temp_x_in, temp_y_in, temp_x_out, temp_y_out
        return False
    

    def reset_en_passant(self, color):
        for j in range(8):
            for i in range(8):
                if isinstance(self.bstruct[i][j], Piece) and self.bstruct[i][j].type == "Pawn":
                    if self.bstruct[i][j].color == color:
                        self.bstruct[i][j].en_passant = False


            
    def check_empty(self):
            dx = (self.x_out - self.x_in > 0) - (self.x_out - self.x_in < 0)
            dy = (self.y_out - self.y_in > 0) - (self.y_out - self.y_in < 0)
            x_ = self.x_in + dx
            y_ = self.y_in + dy

            while (x_, y_) != (self.x_out, self.y_out):
                if self.bstruct[x_][y_] != " ":
                    return False
                x_ += dx
                y_ += dy
            
            if self.bstruct[self.x_out][self.y_out] == " ":
                return True
            
            elif self.bstruct[self.x_out][self.y_out].color != self.color:
                return True
            
            else:
                return False
            
    def move(self):
            if self.bstruct[self.x_in][self.y_in].type == "Pawn":
                if self.bstruct[self.x_in][self.y_in].first_move == True:
                    self.bstruct[self.x_in][self.y_in].en_passant = True
                self.bstruct[self.x_in][self.y_in].first_move = False
            
            self.bstruct[self.x_out][self.y_out] = self.bstruct[self.x_in][self.y_in]
            self.bstruct[self.x_in][self.y_in] = " "

            if self.color == "White":
                self.opp_color = self.color
                self.color = "Black"
            else:
                self.opp_color = self.color
                self.color = "White"

            self.reset_en_passant(self.color)


class Chess_game:

    def __init__(self):
        self.active_player = "white"

        self.white_pieces = []
        self.black_pieces = []

        self.white_attack = np.full((8,8), 0b0)
        self.black_attack = np.full((8,8), 0b0)


        self.fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        self.set_up(self.fen)
        
    def set_up(self, fen):
        rows = fen.split()[0].split('/')

        piece_map = {
            'p': 'pawn', 'r': 'rook', 'n': 'knight', 'b': 'bishop', 'q': 'queen', 'k': 'king',
            'P': 'pawn', 'R': 'rook', 'N': 'knight', 'B': 'bishop', 'Q': 'queen', 'K': 'king',
        }

        for row_index, row in enumerate(rows):
            col_index = 0
            for char in row:
                if char.isdigit():
                    col_index += int(char)
                else:
                    position = np.array([row_index, col_index])
                    piece_type = piece_map[char]
                    image = f"{'w' if char.isupper() else 'b'}_{piece_type}"
                    if char.isupper():
                        color = "white"
                        self.white_pieces.append(Piece(position, piece_type, color, image))
                    else:
                        color = "black"
                        self.black_pieces.append(Piece(position, piece_type, color, image))
                    col_index += 1

        for list in [self.white_pieces, self.black_pieces]:
            for index, piece in enumerate(list):
                piece.piece_id = index

     
    def update_white_attack(self, piece):
        
    def update_black_attack(self):

    def process(self):

    def is_bit_one(number: int, position: int) -> bool:
        mask = 1 << (position)
        return (number & mask) != 0

    

    

    

