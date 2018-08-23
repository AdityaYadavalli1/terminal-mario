class Obstacles:
    """ defining obstacles """

    def __init__(self, length, width, type, side=None):
        self.x = None
        self.y = None
        self.char = []
        self.length = length
        self.width = width
        self.type = type
        self.side = side

    def setNewPosition(self, x, y):
        self.x = x
        self.y = y


class Pipe(Obstacles):
    """ Define Pipes """

    def __init__(self, length, width, type):
        Obstacles.__init__(self, length, width, type)


class Bricks(Obstacles):
    """ Define bricks """

    def __init__(self, length, width, type):
        Obstacles.__init__(self, length, width, type)


class Tort(Obstacles):
    """ Define Tortoise """

    def __init__(self, length, width, type, side):
        Obstacles.__init__(self, length, width, type)
        self.char = ['o', 'O', 'o']
        self.remove = 0

    def sideChange(self):
        if self.x < 28:
            self.x = 28
            self.side = 1
        if self.x > 90:
            self.x = 90
            self.side = -1

    def movetort(self):
        if self.side == 1:
            self.x = self.x + 2
        else:
            self.x = self.x - 2


class BossE(Obstacles):
    def __init__(self, length, width, type, side):
        Obstacles.__init__(self, length, width, type)
        self.char = [['\033[35m' + ' ' + '\033[0m', '\033[35m' + 'R' + '\033[0m', '\033[35m' + 'R' + '\033[0m', '\033[35m' + ' ' + '\033[0m'], ['\033[35m' + '(' + '\033[0m', '\033[35m' + '(' + '\033[0m', '\033[35m' + ')' + '\033[0m', '\033[35m' + ')' + '\033[0m'], [
            '\033[35m' + '^' + '\033[0m', '\033[35m' + '^' + '\033[0m', '\033[35m' + '^' + '\033[0m', '\033[35m' + '^' + '\033[0m']]
        self.remove = 0
        self.health = 3

    def sideChange(self, player):
        if player.x + 40 >= self.x:
            self.side = 1
        if self.x >= 250:
            self.x = 250
        if self.x <= 140:
            self.x = 140
        if player.x + 40 <= self.x:
            self.side = -1

    def moveBossE(self):
        if self.side == 1:
            self.x = self.x + 2
        else:
            self.x = self.x - 2
