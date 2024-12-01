from chess_pieces import Piece
import pandas as pd


class Piece:
    def __init__(self, p_type, color):
        self.type = p_type
        self.color = color

    def __str__(self):
        return self.type

class Board:
    def __init__(self):
        self.bstruct = [[" " for i in range(8)] for j in range(8)]
        #self.bstruct = pd.DataFrame()
        self.set_up()
        self.color = ""

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
            self.bstruct[1][i] = Piece("Pawn", "Black")
            self.bstruct[6][i] = Piece("Pawn", "White")

        # Black Pieces
        self.bstruct[0][0] = Piece("Tower", "Black")
        self.bstruct[0][7] = Piece("Tower", "Black")

        self.bstruct[0][1] = Piece("Knight", "Black")
        self.bstruct[0][6] = Piece("Knight", "Black")

        self.bstruct[0][2] = Piece("Bishop", "Black")
        self.bstruct[0][5] = Piece("Bishop", "Black")

        self.bstruct[0][4] = Piece("King", "Black")
        self.bstruct[0][3] = Piece("Queen", "Black")

        # White Pieces
        self.bstruct[7][0] = Piece("Tower", "White")
        self.bstruct[7][7] = Piece("Tower", "White")

        self.bstruct[7][1] = Piece("Knight", "White")
        self.bstruct[7][6] = Piece("Knight", "White")

        self.bstruct[7][2] = Piece("Bishop", "White")
        self.bstruct[7][5] = Piece("Bishop", "White")

        self.bstruct[7][4] = Piece("King", "White")
        self.bstruct[7][3] = Piece("Queen", "White")

    def process(self, color):
        self.color = color

        in_ = input(f"{self.color}: Where is the piece you want to move? ")
        out_ = input(f"{self.color}: Where do you want to move it? ")

        self.check_legal(int(in_[0]), int(in_[1]), int(out_[0]), int(out_[1]))


    

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

    
    def check_legal(self, x_in, y_in, x_out, y_out):

        def illegal():
            print("Please enter a legal move. Try again.")
            self.process(self.color)
        
        def move():
            self.bstruct[x_out][y_out] = self.bstruct[x_in][y_in]
            self.bstruct[x_in][y_in] = " "

        def check_empty():
            dx = (x_out - x_in > 0) - (x_out - x_in < 0)
            dy = (y_out - y_in > 0) - (y_out - y_in < 0)
            x_ = x_in + dx
            y_ = y_in + dy

            while (x_, y_) != (x_out, y_out):
                if self.bstruct[x_][y_] != " ":
                    illegal()
                x_ += dx
                y_ += dy
    

        obj = self.bstruct[x_in][y_in]

        if obj.color != self.color:
            illegal()

        if (isinstance(obj, Piece) and obj.type == "Pawn"):
            sign = 1
            if obj.color == "White":
                sign = -1
                
            if (x_out - x_in == 0) and (y_out - y_in == sign*1):
                if self.bstruct[x_out][y_out] != " ":
                    illegal()
                else:
                    move()
                

        elif (isinstance(obj, Piece) and obj.type == "Tower"):
            if (x_in != x_out) and (y_in != y_out):
                illegal()
            



        elif (isinstance(obj, Piece) and obj.type == "Knight"):
            pass
        elif (isinstance(obj, Piece) and obj.type == "Bishop"):
            pass
        elif (isinstance(obj, Piece) and obj.type == "King"):
            pass
        elif (isinstance(obj, Piece) and obj.type == "Queen"):
            pass

    def update(self):
        pass



def main():

    board = Board()

    print(
    """
    Let's play chess!

    Please enter coordinates on the form: 12, for the 1 column and the second row.

    White starts the game!

    """)
    

    while True:
        for color in ["White", "Black"]:
            board.print_board()
            board.process(color)
            board.update()




if __name__ == "__main__":
    
    main()