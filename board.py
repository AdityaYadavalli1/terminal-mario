import os
from person import Person
from player import Player
from obstacles import Pipe
from obstacles import Bricks
from obstacles import Tort
from obstacles import BossE
from coins import Coins

player = Player(3, 6, "player")
pipe1 = Pipe(11, 13, "pipe")
pipe1.setNewPosition(25, 50)
pipe2 = Pipe(11, 15, "pipe")
pipe2.setNewPosition(25, 140)
bricks1 = Bricks(8, 5, "bricks")
bricks1.setNewPosition(17, 38)
bricks2 = Bricks(8, 5, "bricks")
bricks2.setNewPosition(17, 97)
#bossE = BossE(3, 4, "bossE", 1)
#bossE.setNewPosition(204, 31)
# coins will be interms of player coordinates
#coinslist = []
#coinslist.append(Coins(12, -10))
#coinslist.append(Coins(20, -10))


class Board:
    """defining the board """

    def __init__(self):
        """making the boarders"""
        self.matrix = [[' '] * 408 for i in range(35)]
        self.store = [[' '] * 6 for i in range(3)]
        self.storetort = [[' '] * 3 for i in range(1)]
        self.storebossE = [[' '] * 4 for i in range(3)]
        self.coinslist = []
        self.coinslist.append(Coins(12, -10))
        self.coinslist.append(Coins(20, -10))
        self.coinslist.append(Coins(52, -11))
        self.coinslist.append(Coins(60, -11))
        self.coinslist.append(Coins(102, -10))
        self.coinslist.append(Coins(110, -10))
        self.coinslist.append(Coins(174, 0))
        self.coinslist.append(Coins(166, 0))

    def makeborder(self):
        for i in range(300):  # height border
            self.matrix[0][i] = '_'
            self.matrix[34][i] = '_'
        for i in range(35):  # width border
            self.matrix[i][0] = '|'
            self.matrix[i][300] = '|'

    def makeclouds1(self):
        for i in range(16):
            self.matrix[4][45 + i] = '\033[36m' + '-' + '\033[0m'
        for i in range(16):
            self.matrix[8][45 + i] = '\033[36m' + '_' + '\033[0m'
        for i in range(4):
            self.matrix[5 + i][61] = '\033[36m' + ')' + '\033[0m'
        for i in range(4):
            self.matrix[5 + i][44] = '\033[36m' + '(' + '\033[0m'

    def makeclouds2(self):
        for i in range(16):
            self.matrix[4][230 + i] = '\033[36m' + '_' + '\033[0m'
        for i in range(16):
            self.matrix[8][230 + i] = '\033[36m' + '_' + '\033[0m'
        for i in range(4):
            self.matrix[5 + i][246] = '\033[36m' + ')' + '\033[0m'
        for i in range(4):
            self.matrix[5 + i][229] = '\033[36m' + '(' + '\033[0m'

    def makepipe1(self):
        for i in range(pipe1.length - 2):
            self.matrix[i + pipe1.x +
                        1][pipe1.y] = '\033[32m' + '|' + '\033[0m'
            self.matrix[pipe1.x][pipe1.y] = '\033[32m' + '(' + '\033[0m'
            self.matrix[pipe1.x][pipe1.y + pipe1.width -
                                 1] = '\033[32m' + ')' + '\033[0m'
        for i in range(pipe1.width - 2):
            self.matrix[pipe1.x][pipe1.y + i +
                                 1] = '\033[32m' + '_' + '\033[0m'
        for i in range(pipe1.width - 2):
            self.matrix[pipe1.x - 1][pipe1.y + i +
                                     1] = '\033[32m' + '_' + '\033[0m'
        for i in range(pipe1.length - 2):
            self.matrix[pipe1.x + i + 1][pipe1.y +
                                         pipe1.width - 1] = '\033[32m' + '|' + '\033[0m'

    def makepipe2(self):
        for i in range(pipe2.length - 2):
            self.matrix[i + pipe2.x +
                        1][pipe2.y] = '\033[32m' + '|' + '\033[0m'
            self.matrix[pipe2.x][pipe2.y] = '\033[32m' + '(' + '\033[0m'
            self.matrix[pipe2.x][pipe2.y + pipe2.width -
                                 1] = '\033[32m' + ')' + '\033[0m'
        for i in range(pipe2.width - 2):
            self.matrix[pipe2.x][pipe2.y + i +
                                 1] = '\033[32m' + '_' + '\033[0m'
        for i in range(pipe2.width - 2):
            self.matrix[pipe2.x - 1][pipe2.y + i +
                                     1] = '\033[32m' + '_' + '\033[0m'
        for i in range(pipe2.length - 2):
            self.matrix[pipe2.x + i + 1][pipe2.y +
                                         pipe2.width - 1] = '\033[32m' + '|' + '\033[0m'

    def makebrick1(self):
        for i in range(0, bricks1.width - 1, 2):
            for j in range(bricks1.length - 1):
                self.matrix[bricks1.x + i][bricks1.y +
                                           j] = '\033[31m' + '-' + '\033[0m'
        for i in range(0, bricks1.length - 1, 2):
            self.matrix[bricks1.x + 1][bricks1.y +
                                       i] = '\033[31m' + '|' + '\033[0m'

    def makebrick2(self):
        for i in range(0, bricks2.width - 1, 2):
            for j in range(bricks2.length - 1):
                self.matrix[bricks2.x + i][bricks2.y +
                                           j] = '\033[31m' + '-' + '\033[0m'
        for i in range(0, bricks2.length - 1, 2):
            self.matrix[bricks2.x + 1][bricks2.y +
                                       i] = '\033[31m' + '|' + '\033[0m'

    def makehill1(self):
        for i in range(15):
            self.matrix[19 + i][211 - i] = '\033[91m' + '/' + '\033[0m'
        for i in range(14):
            self.matrix[20 + i][212 + i] = '\033[91m' + '\\' + '\033[0m'

    def makehill2(self):
        for i in range(15):
            self.matrix[19 + i][120 - i] = '\033[91m' + '/' + '\033[0m'
        for i in range(14):
            self.matrix[20 + i][121 + i] = '\033[91m' + '\\' + '\033[0m'

    def makehill3(self):
        for i in range(15):
            self.matrix[19 + i][24 - i] = '\033[91m' + '/' + '\033[0m'
        for i in range(14):
            self.matrix[20 + i][25 + i] = '\033[91m' + '\\' + '\033[0m'

    def makecoins(self):
        for coins in self.coinslist:
            if coins.remove == 0:
                self.matrix[33 + coins.y][40 +
                                          coins.x] = '\033[93m' + coins.char + '\033[0m'
            else:
                self.matrix[33 + coins.y][40 + coins.x] = ' '

    def util(self):
        self.makeborder()
        self.makehill1()
        self.makehill2()
        self.makehill3()
        self.makepipe1()
        self.makepipe2()
        self.makebrick1()
        self.makebrick2()
        self.makeclouds1()
        self.makeclouds2()
        # self.makecoins()
    # player and tort have their characters in their classes

    def Print(self, player, tort1, bossE):
        """printing the part of the board necessary"""  # y coord is first

        self.util()
        os.system('clear')
        for coins in self.coinslist:  # check collision
            if coins.x == player.x and coins.y == player.y and coins.remove == 0:
                coins.remove = 1
                player.score += 25
        self.makecoins()
        for j in range(3):
            for i in range(6):
                self.store[j][i] = self.matrix[j +
                                               31 + player.y][i + 40 + player.x]
        for i in range(3):
            for j in range(4):
                self.storebossE[i][j] = self.matrix[i +
                                                    31][j + bossE.x]
        for i in range(1):
            for j in range(3):
                self.storetort[i][j] = self.matrix[33][40 + tort1.x + j]
        if tort1.remove == 0:
            for i in range(3):  # tort1
                self.matrix[33][40 + i + tort1.x] = '\033[35m' + \
                    tort1.char[i][0] + '\033[0m'
        if bossE.remove == 0:
            for i in range(3):
                for j in range(4):
                    self.matrix[i + 31][j +
                                        bossE.x] = bossE.char[i][j]

        for j in range(3):  # printing player
            for i in range(6):
                self.matrix[j + 31 + player.y][i +
                                               40 + player.x] = player.char[j][i]
        for i in range(35):
            for j in range(player.x, 204 + player.x):
                print (self.matrix[i][j], end=""),
            print()
        print()

        for j in range(3):  # clearing the player
            for i in range(6):
                self.matrix[j + 31 + player.y][i +
                                               40 + player.x] = self.store[j][i]
        for i in range(1):  # tort1
            for j in range(3):
                self.matrix[33][40 + tort1.x + j] = self.storetort[i][j]

        for i in range(3):
            for j in range(4):
                self.matrix[i + 31][j +
                                    bossE.x] = self.storebossE[i][j]
