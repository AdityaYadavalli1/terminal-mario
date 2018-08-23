from person import Person
import sys


class Player(Person):
    """ Define Player """

    def __init__(self, length, width, person_type):
        Person.__init__(self, length, width, person_type)
        self.char = [['[', '^', '^', '^', '^', ']'],
                     [' ', '[', ']', '[', ']', ' '], [' ', ' ', '[', ']', ' ', ' ']]
        self.health = 5

    def move(self, ch, tort1, bossE):
        if ch == 'w':
            self.jump = True
        if ch == 'a':
            self.Left(tort1, bossE)
        if ch == 'd':
            self.Right(tort1, bossE)
