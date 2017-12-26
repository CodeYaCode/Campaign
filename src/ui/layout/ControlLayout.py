# ControlLayout.py
#!/user/bin/env python3
# -*- coding: utf-8 -*-

'ControlLayout.py'
'@author LiuChen'

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# CONSTANTS

# COLOR
CLOSE_BTN_COLOR = '#F54545'
LOAD_BTN_COLOR  = '#317EF3'
SAVE_BTN_COLOR  = '#5FBA7D'

class ControlLayout(QHBoxLayout):
	"""docstring for ControlLayout"""
	def __init__(self, fClose, widget, **arg):
		super(ControlLayout, self).__init__()
		self.close = fClose
		self.widget = widget
		self.setGeometry(QRect(300, 300, 300, 30))

		# init ui
		self.initUI()

	def initUI(self):
		# close button
		self.closeBtn = QPushButton('X', self.widget)
		self.closeBtn.clicked.connect(self.close)
		self.closeBtn.setStyleSheet(
			'''
				margin: 0px;
				padding: 0px;
				width: 10px;
				height: 10px;
				background-color:%s
			''' % CLOSE_BTN_COLOR
			)
		# self.addWidget(self.closeBtn)

		# load button
		self.loadBtn = QPushButton('Load')
		self.loadBtn.setStyleSheet(
			'''
				margin: 0px;
				width: 50px;
				height : 25px;
				background-color:%s
			''' % LOAD_BTN_COLOR
			)
		self.addWidget(self.loadBtn)

		# save button
		self.saveBtn = QPushButton('Save')
		self.saveBtn.setStyleSheet(
			'''
				margin: 0px;
				width: 50px;
				height: 25px;
				background-color:%s
			''' % SAVE_BTN_COLOR
			)
		self.addWidget(self.saveBtn)
		self.addStretch()

		# version info label

