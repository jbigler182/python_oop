"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    """Machine for finding random words from dictionary.
    
    >>> wf = WordFinder("word.txt")
    3 words read

    >>> wf.random() in ["The", "Ball", "Awake"]
    True
    """

    def __init__(self, path):
        """Read dictionary and reports # items read."""

        file = open(path)

        self.words = self.parse(file)   #A parser is a software component that takes input data (typically text) and builds a data structure

        print(f"{len(self.words)} words read")

    def parse(self, file):
        """Parse dict_file -> list of words."""

        return [w.strip() for w in file]  #remove extra whitespaces and specified characters from the start and from the end of the strip irrespective of how the parameter is passed

    def random(self):
        """Return random word."""

        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("otherwords.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """

    def parse(self, file):
        """Parse file -> list of words, skipping blanks/comments."""

        return [w.strip() for w in file
                if w.strip() and not w.startswith("&")]