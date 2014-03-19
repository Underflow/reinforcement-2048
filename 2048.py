import sys
import os
import time
import PySide.QtWebKit
from ai import AI
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *

def proceed_move():
    timer.stop()
    (score, board) = extract_data()
    if proceed_move.last_score > score:
        ai.restart_game()

    proceed_move.last_score = score
    move = ai.get_move(score, board)
    if move == 0:
        key = Qt.Key_Down
    elif move == 1:
        key = Qt.Key_Up
    elif move == 2:
        key = Qt.Key_Left
    elif move == 3:
        key = Qt.Key_Right
    ev = QKeyEvent(QEvent.KeyPress, key, Qt.NoModifier)

    QCoreApplication.postEvent(web, ev)
    timer.start(100)

proceed_move.last_score = 1000

def extract_data():
    document = web.page().mainFrame()
    game_message = document.findFirstElement(".game-message")
    if game_message.geometry().x() != 0:
        el = document.findFirstElement("a.retry-button");
        el.evaluateJavaScript("this.click()");

    game = [[None, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None]]
    for x in range(0, 4):
        for y in range(0, 4):
            dom_class = ".tile-position-" + str(x + 1) + "-" + str(y + 1)
            tile = document.findFirstElement(dom_class)
            if tile.toPlainText() != '':
                game[y][x] = int(tile.toPlainText()[:-1])
    score = document.findFirstElement(".score-container").toPlainText()
    score = score.split('+')[0]
    if score == '':
        return (0, game)
    else:
        return (int(score), game)

def onFrame(val):
    frame = web.page().mainFrame()
    frame.setScrollBarValue(Qt.Vertical, 40)
    frame.setScrollBarPolicy(Qt.Vertical, Qt.ScrollBarAlwaysOff);

app = QApplication(sys.argv)

web = QWebView()
web.load(QUrl("http://gabrielecirulli.github.io/2048/"))

ai = AI()
web.page().frameCreated.connect(onFrame)
web.show()
timer = QTimer()
timer.timeout.connect(proceed_move)
timer.start(100)

os._exit(app.exec_())
