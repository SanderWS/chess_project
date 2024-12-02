import pygame
import pandas as pd


class Piece:
    def __init__(self, p_type, color, img):
        self.type = p_type
        self.color = color
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
        self.SQUARE_SIZE = 60
        self.x_in = None
        self.x_out = None
        self.y_in = None
        self.y_out = None

    def coordinate_conv(self, a):
        letters = "ABCDEFGH"
        letter_dict = {letter : (numb + 1)  for numb, letter in enumerate(letters)}
        number_dict = {(numb + 1) : letter  for numb, letter in enumerate(letters)}

        if isinstance(a, str) and (a.upper() in letters):
            a = a.upper()
            return number_dict[a]
        elif isinstance(a, int) and (a in range(8)):
            return letter_dict[a]



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
                print("if clause")
                self.illegal()
                return
        
        self.check_legal()



    def print_board(self):
        print()
        df = pd.DataFrame(self.bstruct)
        print(df)
        print()


    def print_board_(self):

        s = ""
        b = ""

        for i in range(8):
            s += "----"

        s += "-"
        for i in range(8):

            b += f"{s}\n"
            for j in range(8):
                if self.bstruct[i][j] == None:
                    b += "|   "
                else:
                    b += "| x "

            b += "|\n"
            
        b += s

        print(b)

    def illegal(self):
        print("illegal!")
    
    def check_legal(self):

        def move():
            if obj.type == "Pawn":
                self.bstruct[self.x_in][self.y_in].first_move = False
            
            self.bstruct[self.x_out][self.y_out] = self.bstruct[self.x_in][self.y_in]
            self.bstruct[self.x_in][self.y_in] = " "

            if self.color == "White":
                self.color = "Black"
            else:
                self.color = "White"
            
            

        def check_empty():
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
                    move()

                elif (self.x_out - self.x_in == sign*2) and (obj.first_move == True):
                    if check_empty():
                        move()

                else:
                    self.illegal()
            else:
                self.illegal()
                

        elif (isinstance(obj, Piece) and obj.type == "Rook"):
            if (self.x_in != self.x_out) and (self.y_in != self.y_out):
                self.illegal()
                return False
            
            elif check_empty():
                move()
                return True
            
            else:
                self.illegal()
                return False
            
            
        elif (isinstance(obj, Piece) and obj.type == "Knight"):
            if (abs(self.x_out - self.x_in) == 2) and (abs(self.y_out - self.y_in) == 1):
                if self.bstruct[self.x_out][self.y_out] == " ":
                    move()
                    return True
            
                elif self.bstruct[self.x_out][self.y_out].color != self.color:
                    move()
                    return True
                
                else:
                    self.illegal()
                    return False

            elif (abs(self.x_out - self.x_in) == 1) and (abs(self.y_out - self.y_in) == 2):
                if self.bstruct[self.x_out][self.y_out] == " ":
                    move()
                    return True
            
                elif self.bstruct[self.x_out][self.y_out].color != self.color:
                    move()
                    return True
                
                else:
                    self.illegal()
                    return False
            else:
                self.illegal()
                return False

            
        elif (isinstance(obj, Piece) and obj.type == "Bishop"):
            if (self.x_out - self.x_in != 0) and (self.y_out - self.y_in != 0):
                if (abs((self.x_out - self.x_in)/(self.y_out - self.y_in)) == 1) and check_empty():
                    move()
                    return True
                    
                else:
                    self.illegal()
                    return False
            else:
                self.illegal()
                return False
            
        elif (isinstance(obj, Piece) and obj.type == "King"):
            if (abs(self.x_out - self.x_in) < 2) and (abs(self.y_out - self.y_in) < 2):
                if check_empty():
                    move()
                    return True
                else:
                    self.illegal()
                    return False
            else:
                self.illegal()
                return False
                    
                
        elif (isinstance(obj, Piece) and obj.type == "Queen"):
            if (self.x_out - self.x_in != 0) and (self.y_out - self.y_in != 0):
                if (abs((self.x_out - self.x_in)/(self.y_out - self.y_in)) == 1) and check_empty():
                    move()
                    return True
                    
                else:
                    self.illegal()
                    return False
                
            elif (self.x_in == self.x_out) or (self.y_in == self.y_out) and check_empty():
                move()
                return True
            
            else:
                self.illegal()
                return False


    def update(self):
        pass
