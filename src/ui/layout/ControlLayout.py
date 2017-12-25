# ControlLayout.py
#!/user/bin/env python3
# -*- coding: utf-8 -*-

'ControlLayout.py'
'@author LiuChen'

import sys

from PyQt5.QtWidgets import *

# CONSTANTS

# COLOR
CLOSE_BTN_COLOR = '#F54545'
LOAD_BTN_COLOR  = '#317EF3'
SAVE_BTN_COLOR  = '#5FBA7D'

class ControlLayout(QHBoxLayout):
	"""docstring for ControlLayout"""
	def __init__(self, fClose, **arg):
		super(ControlLayout, self).__init__()
		self.close = fClose
		# init ui
		self.initUI()

	def initUI(self):
		# close button
		self.closeBtn = QPushButton('X')
		self.closeBtn.clicked.connect(self.close)
		self.closeBtn.setStyleSheet(
			'''
				background-color:%s
			''' % CLOSE_BTN_COLOR
			)
		self.addWidget(self.closeBtn)

		# load button
		self.loadBtn = QPushButton('Load')
		self.loadBtn.setStyleSheet(
			'''
				background-color:%s
			''' % LOAD_BTN_COLOR
			)
		self.addWidget(self.loadBtn)

		# save button
		self.saveBtn = QPushButton('Save')
		self.saveBtn.setStyleSheet(
			'''
				width:100px;
				height:20px;
				background-color:%s
			''' % SAVE_BTN_COLOR
			)
		self.addWidget(self.saveBtn)

		# version info label

