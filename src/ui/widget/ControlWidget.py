# ControlWidget.py
#!/user/bin/env python3
# -*- coding: utf-8 -*-

'ControlWidget.py'
'@author LiuChen'

import sys
import os

from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QLabel, QMenu
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor

# CONSTANTS

# COLOR
CLOSE_BTN_COLOR = '#F54545'
LOAD_BTN_COLOR  = '#317EF3'
SAVE_BTN_COLOR  = '#5FBA7D'

# SIZE
BTN_HEIGHT      = 25
CLOSE_BTN_WIDTH = BTN_HEIGHT
LOAD_BTN_WIDTH  = 200
SAVE_BTN_WIDTH  = 60

# QSS
MAIN_QSS = '''
	QWidget{border: 3px solid green;}
'''

CLOSE_BTN_QSS = '''
	width: %s;
	height: %s;
	color: white;
	border: 0;
	margin: 0;
	background-color: %s;

''' % (CLOSE_BTN_WIDTH, BTN_HEIGHT, CLOSE_BTN_COLOR)

LOAD_BTN_QSS = '''
	width: %s;
	height: %s;
	color: white;
	border: 0;
	margin: 0;
	background-color: %s;

''' % (LOAD_BTN_WIDTH, BTN_HEIGHT, LOAD_BTN_COLOR)

LOAD_MENU_QSS = '''
	width: %s;
	color: white;
	background-color: %s;
''' % (LOAD_BTN_WIDTH, LOAD_BTN_COLOR)

SAVE_BTN_QSS = '''
	width: %s;
	height: %s;
	color: white;
	border: 0;
	background-color: %s;
''' % (SAVE_BTN_WIDTH, BTN_HEIGHT, SAVE_BTN_COLOR)

class ControlWidget(QWidget):
	"""docstring for ControlWidget"""
	def __init__(self, fClose, fLoad, **arg):
		super(ControlWidget, self).__init__()
		# props
		self.close = fClose
		self.load = fLoad
		self.mainLayout = QHBoxLayout(self)
		# 外边距
		self.mainLayout.setContentsMargins(0, 0, 0, 0)
		# 间隙
		self.mainLayout.setSpacing(0)
		# basic conf
		# self.setStyleSheet(MAIN_QSS)
		pal = QPalette(self.palette())
		pal.setColor(QPalette.Background, QColor('#DDD'))
		self.setAutoFillBackground(True)
		self.setPalette(pal)
		# init ui
		self.initUI()

	def initUI(self):
		# close button
		self.closeBtn = QPushButton('X')
		self.closeBtn.clicked.connect(self.close)
		self.closeBtn.setStyleSheet(CLOSE_BTN_QSS)
		self.mainLayout.addWidget(self.closeBtn)

		# # version info label
		# self.versionLabel = QLabel('Version: %s' % ('0.0.1'))
		# self.versionLabel.setStyleSheet('margin-right: 5')
		# self.mainLayout.addWidget(self.versionLabel)

		self.mainLayout.addStretch()

		# load button
		self.loadBtn = QPushButton('Load')
		self.loadBtn.setStyleSheet(LOAD_BTN_QSS)
		# menu
		menu = self.loadMenu()
		self.loadBtn.setMenu(menu);
		self.mainLayout.addWidget(self.loadBtn)

		self.mainLayout.addStretch()

		# save button
		self.saveBtn = QPushButton('Save')
		self.saveBtn.setStyleSheet(SAVE_BTN_QSS)
		self.mainLayout.addWidget(self.saveBtn)

	def setCurrentLabel(self, filename = ''):
		self.loadBtn.setText(filename)

	def getArchive(self):
		rootPath = sys.path[0] + '/src/archive'
		# rootPath = '../archive/'
		# print('current archive path:', rootPath)
		for a, b, c in os.walk(rootPath):
			return c

	def loadMenu(self):
		menu = QMenu()
		menu.setStyleSheet(LOAD_MENU_QSS)
		archive = self.getArchive()
		temp = {}
		for a in archive:
			name = a.split('.')[0]
			temp[name] = name
			menu.addAction(name, lambda name = name : self.load(temp[name]))
		return menu