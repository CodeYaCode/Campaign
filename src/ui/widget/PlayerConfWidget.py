# PlayerConfWidget.py
#!/user/bin/env python3
# -*- coding: utf-8 -*-

'PlayerConfWidget.py'
'@author LiuChen'

import sys

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QInputDialog, QLabel, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette

from src.conf.propConf import propConf

# COLOR
DELETE_BTN_COLOR = '#F54545'
SAVE_BTN_COLOR  = '#5FBA7D'

class PlayerConfWidget(QWidget):
	"""docstring for PlayerConfWidget"""
	def __init__(self, **args):
		super(PlayerConfWidget, self).__init__()
		# props
		# main layout
		self.mainLayout = QHBoxLayout(self)
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
		conf = propConf['player']
		args = args['args']
		print(args)
		for key in conf.keys():
			value = conf[key]
			label = QLabel(value)
			self.mainLayout.addWidget(label)
			self.widgets.append(label)
			if 'player' in args:
				p = args['player']
				btn = QLineEdit(str(p[key]))
				self.mainLayout.addWidget(btn)
				self.widgets.append(btn)
			else:
				edit = QLineEdit()
				self.mainLayout.addWidget(edit)
				self.widgets.append(edit)

		self.mainLayout.addStretch()

		self.saveBtn = QPushButton('Save')
		self.saveBtn.setStyleSheet('border-radius: 0;background-color: %s' % (SAVE_BTN_COLOR))
		self.mainLayout.addWidget(self.saveBtn)

		self.deleteBtn = QPushButton('Delete')
		self.deleteBtn.setStyleSheet('border-radius: 0;background-color: %s' % (DELETE_BTN_COLOR))
		self.mainLayout.addWidget(self.deleteBtn)

	def reset(self):
		for widget in self.widgets:
			self.mainLayout.removeWidget(widget)
			widget.deleteLater()
		self.widgets = []