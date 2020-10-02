import hangman
import string


class Game():
    def __init__(self, player):
        self.player = player
        self.hangman = hangman.Hangman()
    
    def play(self):
        while not self.hangman.is_lost and not self.hangman.is_won:
            self.hangman.display()
            txt = input('Guess a letter, or if you want, guess multiple letters (no spaces) \n')
            for l in list(txt):
                if l not in string.ascii_letters:
                    print(f'{l} is not a valid letter, please try again')
                else:
                    self.hangman.take_input(l.upper())
        self.hangman.display_lost() if self.hangman.is_lost else self.hangman.display_won()
        again = input('Do you want to play again??? Y/N \n')
        if again == 'y' or again == 'Y':
            self.__init__(self.player)
            self.play()

                        

g = Game('ben')
g.play()