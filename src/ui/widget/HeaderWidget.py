# HeaderWidget.py
#!/user/bin/env python3
# -*- coding: utf-8 -*-

'HeaderWidget.py'
'@author LiuChen'

import sys

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit, QPushButton

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

class HeaderWidget(QWidget):
	"""docstring for HeaderWidget"""
	def __init__(self, fAddPlayer, **args):
		super(HeaderWidget, self).__init__()
		# props
		self.addPlayer = fAddPlayer
		self.mainLayout = QHBoxLayout(self)
		# basic conf
		self.mainLayout.setContentsMargins(0, 0, 0, 0)

		# init content
		self.initUI()

	def initUI(self):
		# camp_id
		self.campIdLabel = QLabel('camp_id')
		# self.campIdLabel.setStyleSheet('background-color: lightgray;')
		self.mainLayout.addWidget(self.campIdLabel)
		self.campIdEdit = QLineEdit()
		self.mainLayout.addWidget(self.campIdEdit)
		self.mainLayout.addStretch()

		# map_id
		self.mapIdLabel = QLabel('map_id')
		# self.mapIdLabel.setStyleSheet('background-color: lightgray;')
		self.mainLayout.addWidget(self.mapIdLabel)
		self.mapIdEdit = QLineEdit()
		self.mainLayout.addWidget(self.mapIdEdit)
		self.mainLayout.addStretch()

		# intro
		self.introLabel = QLabel('intro')
		# self.introLabel.setStyleSheet('background-color: lightgray;')
		self.mainLayout.addWidget(self.introLabel)
		self.introEdit = QLineEdit()
		self.mainLayout.addWidget(self.introEdit)

		self.mainLayout.addStretch()

		# addPlayer
		self.addPlayerBtn = QPushButton('Add player')
		self.addPlayerBtn.clicked.connect(self.addPlayer)
		self.addPlayerBtn.setStyleSheet(ADD_BTN_QSS)
		self.mainLayout.addWidget(self.addPlayerBtn)

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