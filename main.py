import game
import colors

class GameRunner():
    def __init__():
        self.game = game.Game()

    def load_game(self):
        pass

t = colors.color('\t\tWelcome to HANGMAN', 'PINK')
print(t)
gr = GameRunner()
running = True
while running:
    i = input('\nPlease choose a mode <new> or <load>')
    if i.lower() == 'new':
        i = gr.game.play()
    elif i.lower() == 'load':
        gr.game = gr.load_game()
        i = gr.game.play()
    elif i.lower() = 'done':
        break
    else: 
        print(f'{colors.color("That is not a valid command, please try again", "RED")}')