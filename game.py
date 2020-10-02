import re
import hangman
import string
import pickle
import os

class Game():
    def __init__(self):
        self.hangman = hangman.Hangman()
        self.loaded = False
    
    def save_game(self):
        files = []
        for (dirpath, dirnames, filenames) in os.walk('.saved-games'):
            files.extend(filenames)
            break
        file_num = 1
        for f in files:
            m = re.search('_(\d+)\.pickle', f)
            if m:
                found = m.group(1)
                if int(found) > file_num:
                    file_num = int(found)
        file_num+=1
        with open(f'.saved-games/hangman_{str(file_num)}.pickle', 'wb') as f:
            pickle.dump(self, f)

    def play(self):
        while not self.hangman.is_lost and not self.hangman.is_won:
            self.hangman.display()
            txt = input('Guess a letter, or if you want, guess multiple letters (no spaces) \n')
            if txt.lower() == 'save':
                self.save_game()
            for l in list(txt):
                if l not in string.ascii_letters:
                    print(f'{l} is not a valid letter, please try again')
                else:
                    self.hangman.take_input(l.upper())
        self.hangman.display_lost() if self.hangman.is_lost else self.hangman.display_won()
        again = input('Do you want to play again??? Y/N or LOAD\n')
        if again.lower() == 'y':
            self.__init__()
            self.play()
        elif txt.lower()=='load':
            return txt.lower()
           
        return 'done'
                   
g = Game()
g.save_game()

