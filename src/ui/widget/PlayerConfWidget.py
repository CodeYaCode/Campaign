# PlayerConfWidget.py
#!/user/bin/env python3
# -*- coding: utf-8 -*-

'PlayerConfWidget.py'
'@author LiuChen'

import sys

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QInputDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette

# COLOR
DELETE_BTN_COLOR = '#F54545'
SAVE_BTN_COLOR  = '#5FBA7D'

class PlayerConfWidget(QWidget):
	"""docstring for PlayerConfWidget"""
	def __init__(self, **args):
		super(PlayerConfWidget, self).__init__()
		# props
		# main layout
		self.mainLayout = QVBoxLayout(self)
		self.mainLayout.setContentsMargins(0, 0, 0, 0)

		self.widgets = []
		# basic conf
		pal = QPalette(self.palette());
		pal.setColor(QPalette.Background, Qt.gray);
		self.setAutoFillBackground(True);
		self.setPalette(pal);
		# init ui
		self.initUI(args)

	def initUI(self, args):
		self.saveBtn = QPushButton('Save')
		self.saveBtn.setStyleSheet('border-radius: 0;background-color: %s' % (SAVE_BTN_COLOR))
		self.mainLayout.addWidget(self.saveBtn)

		self.mainLayout.addStretch()

		self.deleteBtn = QPushButton('Delete')
		self.deleteBtn.setStyleSheet('border-radius: 0;background-color: %s' % (DELETE_BTN_COLOR))
		self.mainLayout.addWidget(self.deleteBtn)
		print(args)