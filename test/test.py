# test.py

import sys

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QApplication


app = QApplication(sys.argv)

win = QWidget()
layout = QVBoxLayout(win)
layout.setContentsMargins(0, 0, 0, 0)
left = QWidget()
left.setStyleSheet('background-color: lightgreen;')
layout.addWidget(left)
leftLayout = QHBoxLayout(left)
leftLayout.addWidget(QLabel('ni'))
leftLayout.addWidget(QLabel('hao'))
leftLayout.setContentsMargins(0, 0, 0, 0)
right = QWidget()
right.setStyleSheet('background-color: lightblue;')
layout.addWidget(right)
rightLayout = QHBoxLayout(right)
rightLayout.addWidget(QLabel('Hello'))
rightLayout.addWidget(QLabel('World'))
rightLayout.setContentsMargins(0, 0, 0, 0)
layout.addStretch()
win.setLayout(layout)
win.show()

sys.exit(app.exec_())