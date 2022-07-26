from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self,path):
        self.path = path
        self.word_list = self.word_list()
        print (f'{len(self.word_list)} words read')

    def __repr__(self):
        return f'Word Finder path = {self.path}'

    def word_list(self):
        file = open(self.path)
        return [line.strip() for line in file]

    def random(self):
        return choice(self.word_list)


