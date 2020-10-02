import game
import colors
import pickle
import os

class GameRunner():
    def __init__(self):
        self.game = game.Game()

    def load_game(self):
        files = []
        for (dirpath, dirnames, filenames) in os.walk('.saved-games'):
            files.extend(filenames)
            break
        print('The following saved games are available:')
        for (i, g) in enumerate(files):
            print(f'Choose {i} to select: ', f'{g[0:-7]}')
        i = input('\nWhich Game would you like to load?\n')
        if int(i) < len(files):
            with open(f'.saved-games/{files[int(i)]}', 'rb') as f:
                self.game = pickle.load(f)
                print('File Loaded\n')
                self.game.loaded = files[int(i)]
        else:
            print('Invalid Choice')

        

t = colors.color('\t\tWelcome to HANGMAN', 'PINK')
print(t)

gr = GameRunner()
running = True
i = ''
while running:
    if i.lower() == 'done':
        break
    i = input('\nPlease choose a mode <new> or <load>\n')
    if i.lower() == 'new':
        gr.game = game.Game()
        i = gr.game.play()
    elif i.lower() == 'load':
        gr.load_game()
        i = gr.game.play()
    else: 
        print(f'{colors.color("That is not a valid command, please try again", "RED")}')