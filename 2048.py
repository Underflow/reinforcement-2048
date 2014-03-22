#! env python2.7

import sys
import os
import time
from ai import AI
from browser import Browser
from PySide.QtCore import *
from PySide.QtGui import *


class Game:
    def __init__(self):
        self.browser = Browser()
        self.app = QApplication(sys.argv)
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateEvent)

        self.ai = AI()
        self.last_score = 1

    def run(self, delay):
        self.timer.start(delay)
        self.browser.run()
        return self.app.exec_()

    def updateEvent(self):
        self.timer.stop()

        (score, board) = self.browser.extractData()

        if self.last_score > score:
            self.ai.restart_game()
        self.last_score = score

        self.browser.sendMove(self.ai.get_move(score, board))

        self.timer.start() # restart the event loop

game = Game()
game.run(10)
