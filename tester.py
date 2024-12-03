
letter_dict = {letter : numb  for numb, letter in enumerate("ABCDEFGH")}
number_dict = {numb : letter  for numb, letter in enumerate("ABCDEFGH")}

text = "12"

#in_ = input("o: Where is the piece you want to move? ")
#out_ = input("o: Where do you want to move it? ")

#print(int(in_[0]), int(in_[1]), int(out_[0]), int(out_[1]))

class Peop:
    def __init__(self, x):
        self.x = x
        self.func()
    def func(self):
        self.x = 2

thing = Peop(1)

print(thing.x)