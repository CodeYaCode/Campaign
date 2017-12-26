# HeaderLayout.py
#!/user/bin/env python3
# -*- coding: utf-8 -*-

'HeaderLayout.py'
'@author LiuChen'

import sys

from PyQt5.QtWidgets import *

# CONSTANTS

# COLOR
ADD_BTN_COLOR  = '#5FBA7D'

# SIZE
BTN_HEIGHT = 25
ADD_BTN_WIDTH  = 80

# QSS
ADD_BTN_QSS = '''
	width: %s;
	height: %s;
	color: white;
	background-color: %s;
	border-radius: 0px;
''' % (ADD_BTN_WIDTH, BTN_HEIGHT, ADD_BTN_COLOR)
# SIZE
CONF_LABEL_WIDTH_PROB = 10

class HeaderLayout(QHBoxLayout):
	"""docstring for HeaderLayout"""
	def __init__(self, fAddPlayer, **args):
		super(HeaderLayout, self).__init__()
		# props
		self.addPlayer = fAddPlayer
		# basic conf
		self.setContentsMargins(0, 0, 0, 0)

		# init content
		self.initUI()

	def initUI(self):
		# camp_id
		self.campIdLabel = QLabel('camp_id')
		# self.campIdLabel.setStyleSheet('background-color: lightgray;')
		self.addWidget(self.campIdLabel)
		self.campIdEdit = QLineEdit()
		self.addWidget(self.campIdEdit)
		self.addStretch()

		# map_id
		self.mapIdLabel = QLabel('map_id')
		# self.mapIdLabel.setStyleSheet('background-color: lightgray;')
		self.addWidget(self.mapIdLabel)
		self.mapIdEdit = QLineEdit()
		self.addWidget(self.mapIdEdit)
		self.addStretch()

		# intro
		self.introLabel = QLabel('intro')
		# self.introLabel.setStyleSheet('background-color: lightgray;')
		self.addWidget(self.introLabel)
		self.introEdit = QLineEdit()
		self.addWidget(self.introEdit)

		self.addStretch()

		# addPlayer
		self.addPlayerBtn = QPushButton('Add player')
		self.addPlayerBtn.clicked.connect(self.addPlayer)
		self.addPlayerBtn.setStyleSheet(ADD_BTN_QSS)
		self.addWidget(self.addPlayerBtn)

	# initial datas
	def initData(self, **args):
		if 'args' in args:
			args = args['args']
		if 'campId' in args:
			self.campIdEdit.setText(str(args['campId']))
		if 'mapId' in args:
			self.mapIdEdit.setText(str(args['mapId']))
		if 'intro' in args:
			self.introEdit.setText(str(args['intro']))