# ControlLayout.py
#!/user/bin/env python3
# -*- coding: utf-8 -*-

'ControlLayout.py'
'@author LiuChen'

import sys
import os

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# CONSTANTS

# COLOR
CLOSE_BTN_COLOR = '#F54545'
LOAD_BTN_COLOR  = '#317EF3'
SAVE_BTN_COLOR  = '#5FBA7D'

# SIZE
BTN_HEIGHT      = 25
CLOSE_BTN_WIDTH = BTN_HEIGHT
LOAD_BTN_WIDTH  = 80
SAVE_BTN_WIDTH  = 60

# QSS
CLOSE_BTN_QSS = '''
	width: %s;
	height: %s;
	font-size: 14px;
	color: white;
	background-color: %s;
	border-radius: 0px;
''' % (CLOSE_BTN_WIDTH, BTN_HEIGHT, CLOSE_BTN_COLOR)

LOAD_BTN_QSS = '''
	width: %s;
	height: %s;
	color: white;
	background-color: %s;
	border-radius: 0px;
''' % (LOAD_BTN_WIDTH, BTN_HEIGHT, LOAD_BTN_COLOR)

SAVE_BTN_QSS = '''
	width: %s;
	height: %s;
	color: white;
	background-color: %s;
	border-radius: 0px;
''' % (SAVE_BTN_WIDTH, BTN_HEIGHT, SAVE_BTN_COLOR)

class ControlLayout(QHBoxLayout):
	"""docstring for ControlLayout"""
	def __init__(self, fClose, fLoad, **arg):
		super(ControlLayout, self).__init__()
		# props
		self.close = fClose
		self.load = fLoad
		# basic conf
		self.setContentsMargins(0, 0, 0, 0)
		# init ui
		self.initUI()

	def initUI(self):
		# close button
		self.closeBtn = QPushButton('X')
		self.closeBtn.clicked.connect(self.close)
		self.closeBtn.setStyleSheet(CLOSE_BTN_QSS)
		self.addWidget(self.closeBtn)

		# load button
		self.loadBtn = QPushButton('Load')
		self.loadBtn.setStyleSheet(LOAD_BTN_QSS)
		# menu
		menu = self.loadMenu()
		self.loadBtn.setMenu(menu);
		self.addWidget(self.loadBtn)

		# save button
		self.saveBtn = QPushButton('Save')
		self.saveBtn.setStyleSheet(SAVE_BTN_QSS)
		self.addWidget(self.saveBtn)

		# current file info
		self.currentLabel = QLabel('Current campaign: %s' % (''))
		self.addWidget(self.currentLabel)

		self.addStretch()

		# version info label
		self.versionLabel = QLabel('Version: %s' % ('0.0.1'))
		self.addWidget(self.versionLabel)

	def setCurrentLabel(self, filename = ''):
		self.currentLabel.setText('Current campaign: %s' % (filename))

	def getArchive(self):
		rootPath = sys.path[0] + '/src/archive'
		# rootPath = '../archive/'
		# print('current archive path:', rootPath)
		for a, b, c in os.walk(rootPath):
			return c

	def loadMenu(self):
		menu = QMenu()
		archive = self.getArchive()
		temp = {}
		for a in archive:
			name = a.split('.')[0]
			temp[name] = name
			menu.addAction(name, lambda name = name : self.load(temp[name]))
		return menu