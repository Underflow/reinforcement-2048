import sys
import PySide.QtWebKit
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *

class Browser:
    def run(self):
        self.web = QWebView()
        self.web.load(QUrl("http://gabrielecirulli.github.io/2048/"))

        self.web.page().frameCreated.connect(self.onInit)
        self.web.show()

    def onInit(self, val):
        frame = self.web.page().mainFrame()
        frame.setScrollBarValue(Qt.Vertical, 40)
        frame.setScrollBarPolicy(Qt.Vertical, Qt.ScrollBarAlwaysOff);

    def sendMove(self, move):
        key = { 0 : Qt.Key_Down,
                1 : Qt.Key_Up,
                2 : Qt.Key_Left,
                3 : Qt.Key_Right }
        ev = QKeyEvent(QEvent.KeyPress, key[move], Qt.NoModifier)
        QCoreApplication.postEvent(self.web, ev)

    def extractData(self):
        document = self.web.page().mainFrame()

        # Try to restart game if finished
        game_message = document.findFirstElement(".game-message")
        if game_message.geometry().x() != 0:
            el = document.findFirstElement("a.retry-button");
            el.evaluateJavaScript("this.click()");

        game = [[None, None, None, None],
                [None, None, None, None],
                [None, None, None, None],
                [None, None, None, None]]

        # Extract board informations from the DOM
        for x in range(0, 4):
            for y in range(0, 4):
                dom_class = ".tile-position-" + str(x + 1) + "-" + str(y + 1)
                tile = document.findFirstElement(dom_class)
                if tile.toPlainText() != '':
                    game[y][x] = int(tile.toPlainText()[:-1])

        # Extract the score
        score = document.findFirstElement(".score-container").toPlainText()
        score = score.split('+')[0]
        score = 0 if score == '' else int(score)

        return (score, game)
