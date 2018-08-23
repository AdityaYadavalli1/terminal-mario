import time


class Person:
    """ Player and enemies class """

    def __init__(self, length, width, type):
        self.length = length
        self.width = width
        self.type = type
        self.char = []
        self.down = False
        self.x = None
        self.y = None
        self.jump = None
        self.prevjump = None
        self.time = time.time()
        self.score = 0

    def setNewPosition(self, x, y):  # call this function once the object is made
        self.x = x
        self.y = y

    def Left(self, tort1, bossE):
        self.x = self.x - 8
        self.y = self.y
        self.score += 5
        if self.x < -32:  # left border
            self.x = -32
            self.score -= 5
        if self.x <= 24 and self.x > 4 and self.y >= -8:  # pipe1
            self.x = 24
            self.score -= 5
        if self.x <= 115 and self.x > 92 and self.y >= -8:  # pipe2
            self.x = 115
            self.score -= 5

    def Right(self, tort1, bossE):
        self.x = self.x + 8
        self.y = self.y
        self.score += 5
        if self.x >= 198:  # right border
            self.x = 198
            self.score += 5
        if self.x >= 8 and self.y >= -8 and self.x < 21:  # for pipe1
            self.x = 4
            self.score -= 5
        if self.x >= 90 and self.y >= -8 and self.x < 111:  # for pipe2
            self.x = 94
            self.score -= 5

    def Jump(self, tort1, bossE):  # isJump always run this function
        if self.jump == True:
            self.prevjump = True
            if self.down == True:
                self.y = self.y + 2
            #    print('going down')
            if self.down == False:
                self.y = self.y - 2
            #    print('going up')
            if self.y <= -16:
                self.down = True
            #    print('reached limit')
            if self.y >= 0:  # or initial value
                #    print('stop')
                self.down = False
                self.jump = False
                self.y = 0
            if self.x > 4 and self.x < 21:  # pipe1
                self.y = -10
                self.down = True
            if self.x > 94 and self.x < 112:  # pipe2
                self.y = -10
                self.down = True
            if self.x >= -8 and self.x <= 4 and self.y < -11:  # for brick1
                self.y = -11
                self.down = True
            if self.x >= 52 and self.x <= 62 and self.y < -11:  # for brick2
                self.y = -11
                self.down = True
        if self.prevjump == True and self.x + 3 >= tort1.x - 1 and self.x - 3 <= tort1.x + 1 and self.y == 0 and tort1.remove == 0:  # for tort killing
            tort1.remove = 1
            self.score += 50
        if self.prevjump == True and self.x + 43 >= bossE.x - 2 and self.x - 37 <= bossE.x + 2 and self.y == 0 and bossE.health == 0:  # for boss removing
            bossE.remove = 1
        if self.prevjump == True and self.x + 42 >= bossE.x - 2 and self.x - 38 <= bossE.x + 2 and self.y == 0 and bossE.remove == 0:  # for boss killing
            bossE.health = bossE.health - 1
            if bossE.x + 14 < 250:
                bossE.x = bossE.x + 20
            else:
                bossE.x = bossE.x - 20
            self.score += 100
        if self.jump == False:
            self.prevjump = False
