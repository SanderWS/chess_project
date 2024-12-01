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

    def process(self, player):
        pass
        
    

    def print_as_pd(self):

        df = pd.DataFrame(self.bstruct)
        print(df)


    def print_board(self):

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

    

    def check_legal(self, from_1, from_2, to_1, to_2):

        def illegal():
            print("Please enter a legal move. Try again.")
            

        obj = self.bstruct[from_1][from_2]
        if (isinstance(obj, Piece) and obj.type == "Pawn"):
            pass

        elif (isinstance(obj, Piece) and obj.type == "Tower"):
            if (from_1 != to_1) and (from_2 != to_2):
                illegal()
            



        elif (isinstance(obj, Piece) and obj.type == "Knight"):

        elif (isinstance(obj, Piece) and obj.type == "Bishop"):

        elif (isinstance(obj, Piece) and obj.type == "King"):

        elif (isinstance(obj, Piece) and obj.type == "Queen"):

    def update(self):
        pass

def main():

    board = Board()
    

    while True:

        player1 = input("Enter a square from and a square to")
        board.process(player1)
        board.check_legal()
        board.update()
        board.print_board()

        player2 = input("Enter a square from and to")
        board.process(player2)
        board.check_legal()
        board.update()
        board.print_board()



if __name__ == "__main__":
    
    main()