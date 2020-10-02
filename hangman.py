import colors
from images import image_dict
import random
import string

def generate_solution():
    with open('words.txt', 'r') as f:
        words = []
        reader = f.read()
        for line in reader.split('\n'):
            if len(line) >= 5 and len(line) <=12:
                words.append(line)
    return random.choice(words).upper()


class Hangman():
    def __init__(self):
        self.solution = generate_solution()
        self.person = Person()
        self.used = set()
        self.incorrect = []
        self.puzzle = ['_']*len(self.solution)

    def display(self):
        print(self.person.image)
        print('PUZZLE: ', ' '.join(self.puzzle))
        txt = colors.color(', '.join(self.incorrect), 'RED')
        print(f'Incorrect Letters: {txt}')

    def display_lost(self):
        print(self.person.image)
        print('PUZZLE: ', ' '.join(self.puzzle))
        print('\t\t'+f'{colors.color("======== GAME OVER ========", "PINK")}')
        print(f'The correct solution was {self.solution}')

    def display_won(self):
        print(self.person.image)
        print('PUZZLE: ', ' '.join(self.puzzle))
        print('\t\t'+f'{colors.color("======== YOU WIN ========", "PINK")}')

    def is_correct(self, char):
        if char in self.solution:
            return True
        return False

    def is_used(self, char):
        if char in self.used:
            return True
        return False

    def take_input(self, char):
        if self.is_correct(char):
            self.correct_guess(char)
        elif self.is_used(char):
            print(f'{char.upper()} has already been guessed')
        else:
            self.incorrect_guess(char)

    @property
    def is_lost(self):
        return not self.person.stage < 6

    @property
    def is_won(self):
        return ''.join(self.puzzle) == self.solution

    def correct_guess(self, char):
        #update self.puzzle
        for (i, l) in enumerate(self.solution):
            if l == char:
                self.puzzle[i] = l

        #update self.used
        self.used.add(char)

    def incorrect_guess(self, char):
        self.used.add(char)
        self.incorrect += [char]
        self.person.add_body_part()




class Person():
    def __init__(self):
        self.stage = 0
        self.lookup = image_dict

    def add_body_part(self):
        if self.stage < 6:
            self.stage +=1

    @property
    def image(self):
        return self.lookup[self.stage]

    