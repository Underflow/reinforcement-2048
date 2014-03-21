import sys
import os
import time
import PySide.QtWebKit
from ai import AI
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *

def proceed_move():
    timer.stop() # to avoid timer to tick during AI decision

    # Is it a new game ?
    (score, board) = extract_data()
    if proceed_move.last_score > score:
        ai.restart_game()

    # Send the move to QtWebkit
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

    # Restart the timer for the next action
    timer.start()
proceed_move.last_score = 1


def extract_data():
    document = web.page().mainFrame()

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

def onFrame(val):
    # Disable QtWebkit scrollbar
    frame = web.page().mainFrame()
    frame.setScrollBarValue(Qt.Vertical, 40)
    frame.setScrollBarPolicy(Qt.Vertical, Qt.ScrollBarAlwaysOff);

# Initialize AI
ai = AI()

# Start a new QtWebkit application and load 2048
app = QApplication(sys.argv)

web = QWebView()
web.load(QUrl("http://gabrielecirulli.github.io/2048/"))

web.page().frameCreated.connect(onFrame)
web.show()

# Launch the action timer to start playing
timer = QTimer()
timer.timeout.connect(proceed_move)
timer.start()

os._exit(app.exec_())
