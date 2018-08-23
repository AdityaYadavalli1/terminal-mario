from board import Board
import os
import sys
from input import Get, input_to
from player import Player
from obstacles import Tort
from obstacles import BossE
import time


class Run:
    def __init__(self):
        self.getch = Get()
        self.player = Player(3, 6, 'player')
        self.player.setNewPosition(0, 0)
        self.board = Board()
        self.tort1 = Tort(1, 1, "tortoise", 1)
        self.tort1.setNewPosition(24, 0)
        self.bossE = BossE(3, 4, "bossE", 1)
        self.bossE.setNewPosition(204, 0)

    def start(self):
        while True:
            #os.system("aplay -q Theme-Ringtone.mp3 &")
            input = input_to(self.getch)
            self.board.Print(self.player,
                             self.tort1, self.bossE)
            print('Press q to quit')
            if self.player.x > 118:
                print('Level 2')
            else:
                print('Level 1')
            if input is not None:
                self.player.move(input, self.tort1, self.bossE)
            self.player.Jump(self.tort1, self.bossE)
            self.tort1.sideChange()
            self.tort1.movetort()
            if self.player.x >= 118:
                if self.player.jump == False:
                    self.bossE.sideChange(self.player)
                    self.bossE.moveBossE()
                else:
                    self.bossE.moveBossE()
                if self.bossE.x <= 160:
                    self.bossE.x = 160
                    self.bossE.sideChange(self.player)
                elif self.bossE.x >= 250:
                    self.bossE.x = 250
                    self.bossE.sideChange(self.player)
            if self.player.x + 43 >= self.bossE.x - 2 and self.player.x - 37 <= self.bossE.x + 2 and self.player.y == 0 and self.player.prevjump == False and time.time() - self.player.time >= 2:  # for boss killing
                if self.bossE.remove == 0:
                    self.player.health = self.player.health - 1
                    self.player.time = time.time()
            if self.player.prevjump == False and self.player.x + 3 >= self.tort1.x - 1 and self.player.x - 3 <= self.tort1.x + 1 and self.player.y == 0 and time.time() - self.player.time >= 2:  # for tort killing
                if self.tort1.remove == 0:
                    self.player.health = self.player.health - 1
                    self.player.time = time.time()
            print("Player Live(s) Left:")
            print(self.player.health)
            print("Boss Enemy Live(s) Left:")
            print(self.bossE.health)
            print("Player Score:")
            print(self.player.score)
            print(self.player.x)
            print(self.player.y)
            if self.bossE.remove == 1 and self.tort1.remove == 1:
                print('Game Over: You won !')
                sys.exit()
            if self.player.health == 0:
                print('Game Over: You lost !')
                sys.exit()
            if self.bossE.remove == 1 and self.tort1.remove == 0:
                print('Go back and kill the Tortoise')
            if input == 'q':
                os.system('clear')
                sys.exit()


run = Run()
run.start()
