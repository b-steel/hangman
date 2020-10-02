import re
import hangman
import string
import pickle
import os

class Game():
    def __init__(self):
        self.hangman = hangman.Hangman()
        self.loaded = False
    
    def delete_file(self):
        os.remove(f'.saved-games/{self.loaded}')

    def save_game(self):
        files = []
        for (dirpath, dirnames, filenames) in os.walk('.saved-games'):
            files.extend(filenames)
            break
        file_num = 0
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
        if self.loaded:
            self.delete_file()

        while not self.hangman.is_lost and not self.hangman.is_won:
            self.hangman.display()
            txt = input('Guess a letter, or if you want, guess multiple letters (no spaces) \n')
            if txt.lower() == 'save':
                self.save_game()
                break
            for l in list(txt):
                if l not in string.ascii_letters:
                    print(f'{l} is not a valid letter, please try again')
                else:
                    self.hangman.take_input(l.upper())
        
        self.hangman.display_lost() if self.hangman.is_lost else self.hangman.display_won() if self.hangman.is_won else print('\n')
        again = input('Do you want to play again??? Y/N\n')
        if again.lower() == 'y':
            return 'again'
        return 'done'
                   

